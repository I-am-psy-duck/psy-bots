import platform
import zipfile
from pathlib import Path
import wget
import os
import json
from .Bot import Action

linux = "https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip"
windows="https://chromedriver.storage.googleapis.com/2.45/chromedriver_win32.zip"
mac = "https://chromedriver.storage.googleapis.com/2.45/chromedriver_win32.zip"
directory = "chromeDriver"

def deleteZipDownloadAfterExtract(file):
    os.remove(file)

def downloadFile():
    """
    If the file does not exits, we will download it
    """
    file = None
    if platform.system() == "Linux":
        file = wget.download(linux)
    elif platform.system() == "Windows":
        file = wget.download(windows)
    else:
        file = wget.download(mac)
    """
    Returns the name of the file as a zip extention
    """
    return file

def unzipFile(file):
    """
    Unzip the file, and then delete it
    """
    with zipfile.ZipFile(file, "r") as zip:
        zip.extractall(directory)
    deleteZipDownloadAfterExtract(file)

def getChromeDriver():
    """
    Get chromeDriver file
    """
    file = Path(directory)
    if file.exists():
        file = Path(directory + "/chromedriver")
        if file.exists():
            os.chmod(directory + "/chromedriver", 0o775)
            return directory + "/" + file.name
        else:
            file = downloadFile()
            unzipFile(file)
            getChromeDriver()
     
    else:
        file = downloadFile()
        unzipFile(file)
        getChromeDriver()

def convertElementTextToInt(element:str):
    try:
        return  int(element.replace(",",""))
    except ValueError as e:
        print("Error while parsing: {}".format(element))
        # TODO refactor it
        return 10000
   
def askForNumber(msg:str):
    try:
        value = str(input(msg))
        if value == "":
            return None
        return int(value)
    except ValueError as e:
        print("Not a valid number: {}".format(s))
        return None

def askForText(msg:str):
    value = str(input(msg))
    if value == "":
        return None
    return value

def createDirectory(directory:str):
    images = Path(directory)
    if not images.exists():
        os.mkdir(directory)
    return directory

# reads a json file and then convert it to dictionary
def readFromJsonFile(file_name : str):
    file = open(file_name, "r")
    json_data = json.load(file)
    bot = json_data["bot"]
    json_actions = json_data["actions"]
    actions = []
    for action in json_actions:
        actions.append(Action[str(action).upper()])
    users = json_data["users"] 
    return {
        "bot":bot,
        "actions":actions,
        "users":users
    }
    

def psyduck():
    print("\n\n\n")
    print("\033[1;33;40m            -------   -------  \     /       -----       |      |       -------      |    /        ")
    print("\033[1;37;40m            |     |  /          \   /        |     \     |      |      /             |   /         ")
    print("\033[1;33;40m            |     |  \           \ /         |      \    |      |     /              |  /          ")
    print("\033[1;37;40m            |-----    -----       |          |       |   |      |    |               | /           ")
    print("\033[1;33;40m            |              \      |          |      /    |      |     \              | \           ")
    print("\033[1;37;40m            |              /      |          |     /     |      |      \             |  \          ")
    print("\033[1;33;40m            |        ------       |          -----        ------        -------      |   \         ")
    print("\033[5;37;40m                                             Author: psyduck3@protonmail.com                       ")
    print("\n\n\n")
