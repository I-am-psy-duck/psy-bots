from booter.Bot import Bot, Action
from booter.Connection import Connection, BotConnect
from InstagramAction import InstagramAction
from booter.Credentials import Credentials
from booter.bot_util import askForNumber, askForText, readFromJsonFile
from exceptions.BotException import BotNotFoundExeption 
from booter.Store import  StoreDatabase, StoreFile


connection = Connection()
BOT_TYPE = "INSTAGRAM"

def isAvailableBot(bot_name:str):
    return BotConnect().findBotByName(bot_name)

def createBot(bot_id : int, bot_name:str):
    data = isAvailableBot(bot_name)

    # if was not found a bot
    if data is None:
        raise BotNotFoundExeption(bot_name)
    credentials = Credentials(data[0], data[1], data[2], data[3])
    return Bot(credentials, bot_id)
   
def findData(action:Action):
    return connection.findInitalData(BOT_TYPE, action.value)

def initBot(action:Action, bot_name:str):
    data = findData(action)
    bot = createBot(data[0], bot_name)
    bot.addActionUrl(Action.LOGIN, data[1], data[2])
    return bot

def doAction(username:str, action:Action, bot_name:str, save:bool):
    try:
        bot = initBot(Action.LOGIN, bot_name)
        instagram_action = InstagramAction(bot, connection)
        
        store = None
        if save == True:
            store =  StoreDatabase(connection)
        else:
            store = StoreFile()

        instagram_action.login()

        data = findData(action)
        bot.addActionUrl(action, data[1], data[2])

        if action == Action.FOLLOW:

            instagram_action.followUser(username)

        elif action == Action.FOLLOWING:

            max = askForNumber("If you want to insert a max, type a number")
            instagram_action.getUserFollowing(username, max)

        elif action == Action.FOLLOWERS:

            max = askForNumber("If you want to insert a max, type a number:")
            instagram_action.getFollowingUser(username, max)

        elif action == Action.LIKE_POST:

            max = askForNumber("If you want to insert a max posts to like, type a number:")
            number_comments = askForNumber("If you want to insert comments, type how many you want:")
            comments = []
            while len(comments) != number_comments:
                if number_comments is not None:
                    comment = askForText("Comment: ")
                    if comment is not None and len(comment) > 0:
                        comments.append(comment)
                    else:
                        print("Comment not inserted to comments list!")
            instagram_action.likeUserPhoto(username, comments, max)  

        elif action == Action.DOWNLOAD:
           sources = instagram_action.downloadPhotos(username)
           store.downloadAction(sources, username, bot)    
        
        
        instagram_action.close()
    except Exception as e:
        # Verify if variable exists
        #https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists        
        if "instagram_action" in locals():
            instagram_action.close(e)

def doActionFromJson(file_name: str):
    
    # JSON converted to Python
    data_from_json = readFromJsonFile(file_name)
    
    bot = initBot(Action.LOGIN, data_from_json.get("bot"))
    instagram_action = InstagramAction(bot, connection)

    save = False

    store = None
    if save == True:
        store =  StoreDatabase(connection)
    else:
        store = StoreFile()

    instagram_action.login()
    
    for user in data_from_json.get("users"):
        for action in data_from_json.get("actions"):
            data = findData(action)
            bot.addActionUrl(action, data[1], data[2])

# create a method to this
            if action == Action.FOLLOW:

                instagram_action.followUser(user)

            elif action == Action.FOLLOWING:

                max = askForNumber("If you want to insert a max, type a number")
                instagram_action.getUserFollowing(user, max)

            elif action == Action.FOLLOWERS:

                max = askForNumber("If you want to insert a max, type a number:")
                instagram_action.getFollowingUser(user, max)

            elif action == Action.LIKE_POST:

                max = askForNumber("If you want to insert a max posts to like, type a number:")
                number_comments = askForNumber("If you want to insert comments, type how many you want:")
                comments = []
                while len(comments) != number_comments:
                    if number_comments is not None:
                        comment = askForText("Comment: ")
                        if comment is not None and len(comment) > 0:
                            comments.append(comment)
                        else:
                            print("Comment not inserted to comments list!")
                instagram_action.likeUserPhoto(user, comments, max)  

            elif action == Action.DOWNLOAD:
               sources = instagram_action.downloadPhotos(user)
               store.downloadAction(sources, user, bot)    
        
        
    instagram_action.close()







