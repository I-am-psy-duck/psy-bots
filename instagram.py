from instagram_options import doAction, Action, findData, isAvailableBot, doActionFromJson
from InstagramAction import InstagramAction
from exceptions.BotException import UsernameException
import requests
from booter.bot_util import psyduck
from os import system as os_system
from platform import system
from sys import argv

if system() == "Linux":
    os_system("clear")
else:
    os_system("cls")

actions = {
    "follow" : Action.FOLLOW,
    "following": Action.FOLLOWING,
    "followers": Action.FOLLOWERS,
    "like":Action.LIKE,
    "download":Action.DOWNLOAD
}
#http://ozzmaker.com/add-colour-to-text-in-python/

# PSY DUCK LOGO
psyduck()

bot = ""
username = ""
option = ""


# will read a json file
if len(argv) > 1:
    file_name = argv[1]
    doActionFromJson(file_name)

else:

    try: 

        while bot == "":

            bot = str(input("\033[1;32;40m \n Type the name of the bot: "))
            if  not isAvailableBot(bot):
            
                print("\033[1;31;40m \n Bot with the name: {} was not found!".format(bot))
                bot = ""

        while option == "":

            option = str(input("\033[1;32;40m \n Type the bot action: "))

            if option not in actions:
                print("\033[1;31;40m \n Invalid action!")
                option = ""

        action = actions.get(option)

        while username == "":
            username = str(input("\033[1;32;40m \n Type the username: "))
            action_url = findData(action)[2]
            HTTP_STATUS = requests.get(action_url + username).status_code

            if HTTP_STATUS != 200:
                print("\033[1;31;40m \n Username: {} was not found!".format(username))
                username = ""

            
        doAction(username, action, bot, False)
    except KeyboardInterrupt:
        print("\033[1;31;40m \n User interrupted!")