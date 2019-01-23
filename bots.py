from booter.Connection import BotConnect
from sys import argv
from booter.bot_util import askForText, createDirectory
import json


if len(argv) > 1:

    botConnect = BotConnect()

    if argv[1] == '--create':

        items = []
        items.append(askForText("Description: "))

        while True:
            name = askForText("Name: ")
            bot = botConnect.findBotByName(name)

            if bot == None:
                items.append(name)
                break
            else:
                print("Another bot is using the name: {}".format(name))

        items.append(askForText("E-mail: "))
        items.append(askForText("Login: "))
        items.append(askForText("Phone: "))
        password = None

        while password == None:
            password = askForText("Password: ")
        items.append(password)
        botConnect.createBot(items)

    elif argv[1] == '--show':
        bots = botConnect.availableBots()
        for bot in bots:
            print("\n   Description: {} \n   BOT_NAME: {}\n".format(bot[0], bot[1]))

    elif argv[1] == '--generate':
        # create a file
        DIRECTORY = createDirectory("instagram-json")
        file_name = askForText("File name: ")

        data = {}
        data["bot"] = str(input("Bot name: "))

        actions = ["follow", "followers", "following", "like", "download"]

        options = []
        print("Type .exit to finish with actions")

        while True:
            opt = askForText("Action:")
            if opt == ".exit" and len(options) > 0:
                break
            if opt in actions:
                options.append(opt)
                del actions[actions.index(opt)]
            else:
                print("Invalid action or already used!")


        data["actions"] = options
        users = []
        
        print("Type .exit to finish with users")
        while True:
            name = askForText("Username: ")
            if name == ".exit" and len(users) > 0:
                break
            elif name.strip() != "" :
                users.append(name)

        data["users"] = users
        json_data = json.dumps(data)
        file = open(DIRECTORY + "/" + file_name + ".json", "w")
        file.write(json_data)
        print("File saved!")

    else:
        print("Invalid option!") 

else:
    print("You need to specify a option")

