from .Connection import Connection
from .Bot import Bot, Action

def findInitalData(botName:str, action:Action, connection:Connection):
    # we are using enums here
    value = connection.findInitalData(botName, action.value)
    return value

def findByXpath(bot: Bot, action:Action, connection:Connection, position:int = None):
    # we are using enum
    value = connection.findByXpath(bot.botId, bot.actionUrlIds.get(action.value), position)
    return value[0]

def findFilePath(bot_description:str, connection:Connection):
    value = connection.findFilePath(bot_description)
    return value

def createUser(url:str, connection:Connection):
    success = connection.createUser(url)
    if success:
        print("Success saving the user: {}".format(url))