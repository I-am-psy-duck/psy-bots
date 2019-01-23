from abc import ABC, abstractclassmethod
from .Request import RequestSource 
from .bot_util import createDirectory  
from .Connection import Connection
from .Bot import Bot, Action

class Store(ABC):

    @abstractclassmethod
    def downloadAction(self, sources:list, username:str, bot:Bot):
        pass

class StoreDatabase(Store):
    def __init__(self, connection:Connection):
        self.connection = connection
    
    def downloadAction(self, sources:list, username:str, bot:Bot):
        user_url = bot.urls.get(Action.DOWNLOAD.value) + username
        user_id = self.connection.findOrCreateUser(user_url)
        print("Saving to database ... ")
        for src in sources:
            self.connection.createUserPostSource(user_id, src)
        

class StoreFile(Store):
    def __init__(self):
        self.request_source = RequestSource()

    def downloadAction(self, sources:list, username:str, bot:Bot):
        DIRECTORY = createDirectory("images")
        INSTAGRAM = createDirectory( DIRECTORY + "/instagram") 
        USER_DIRECTORY = createDirectory( INSTAGRAM + "/" + username )
        for i in range(len(sources)):
            image_name = USER_DIRECTORY + "/" + username + "_" + str(i) + ".jpg"
            self.request_source.downloadFromSource(sources[i], image_name)
        


