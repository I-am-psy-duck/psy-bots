class UsernameException(Exception):
    def __init__(self, username:str):
        print("The username: {} is not valid!".format(username))

class BotNotFoundExeption(Exception):
    def __init__(self, bot_name:str):
        print("Bot {} not found!".format(bot_name))