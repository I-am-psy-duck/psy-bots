from .Credentials import Credentials
from enum import Enum, unique

@unique
class Action(Enum):
    """
    Possible actions for that the bot can do
    """
    LOGIN = 'LOGIN'
    FOLLOW = 'FOLLOW'
    FOLLOWING = 'FOLLOWING'
    FOLLOWERS = 'FOLLOWERS'
    LIKE = 'LIKE'
    STORY = 'STORY'
    DOWNLOAD = 'DOWNLOAD'

class Bot():
    def __init__(self, credentials : Credentials, botId:int):
        self.credentials = credentials
        self.botId = botId
        self.actionUrlIds = {} #dictionary to actios of bot
        self.urls = {} #dictionary to urls

    def addActionUrl(self, action: Action, actionUrlId:int, url:str ):
        if action.value not in self.actionUrlIds:
            self.actionUrlIds[action.value] = actionUrlId
            self.urls[action.value] = url