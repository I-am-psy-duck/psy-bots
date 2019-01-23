import sqlite3
from sqlite3 import Error, Row
from .Bot import Action

class Connection:

    def __init__(self):
        self.path = "database/rambot.db"
        self.connection = sqlite3.connect(self.path)
  
    def connect(self):
        self.connection = sqlite3.connect(self.path)
  
    def selectFrom(self, script:str, *queryParameters):
        """
        queryParameters is a varargs to use with preparedStatements ?, ?
        """
        sql = self.connection.cursor()
        sql.execute(script, queryParameters)
        return sql.fetchall()

    def selectOne(self, script:str, *queryParameters):

        sql = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row
        sql.execute(script, queryParameters)
        row = sql.fetchone()
        return tuple(row) if row is not None else row
        #return tuple(row)
    
    def save(self, script:str, *queryParameters):

        sql = self.connection.cursor()
        try:
            sql.execute(script, queryParameters)
            self.connection.commit()
            return True
        except Error as e:
            print(e)
            print("Error while executing: {}".format(script))
            self.connection.rollback()
            return False

    def findInitalData(self, botName:str, actionName:str):
        sql =  " SELECT B.BOT_ID, AU.ACTION_URL_ID, U.URL FROM TB_URL U "
        sql += " INNER JOIN TB_ACTION_URL AU ON U.URL_ID = AU.URL_ID "
        sql += " INNER JOIN TB_BOT_ACTION_URL BAU ON AU.ACTION_URL_ID = BAU.ACTION_URL_ID "
        sql += " INNER JOIN TB_BOT B ON B.BOT_ID = BAU.BOT_ID  "
        sql += " INNER JOIN TB_ACTION A ON A.ACTION_ID = AU.ACTION_ID "
        sql += " WHERE B.DESCRIPTION = ? AND A.DESCRIPTION = ?"
        value = self.selectOne(sql, botName, actionName)
        return value
      
    def findByXpath(self, botId:int, actionUrlId: int, position : int = None):
        sql =  " SELECT X.XPATH, BAUX.DESCRIPTION FROM TB_XPATH X "
        sql += " INNER JOIN TB_BOT_ACTION_URL_XPATH BAUX ON X.XPATH_ID = BAUX.XPATH_ID "
        sql += " INNER JOIN TB_BOT_ACTION_URL BAU ON BAUX.BOT_ACTION_URL_ID = BAU.BOT_ACTION_URL_ID "
        sql += " WHERE BAU.BOT_ID = ? AND BAU.ACTION_URL_ID = ? "
        if position is not None:
            sql += " AND BAUX.POSITION = ? OR BAUX.POSITION IS NULL "
            return self.selectOne(sql, botId, actionUrlId, position)
        else :
            return self.selectOne(sql, botId, actionUrlId)

    def findFilePath(self, bot_description:str):
        sql =  " SELECT PATH FROM TB_FILE_PATH "
        sql += " WHERE BOT_ID = ( SELECT BOT_ID FROM TB_BOT WHERE DESCRIPTION = ? ) "
        return self.selectOne(sql, bot_description)[0]

    def createUser(self, url:str):
        sql =  " INSERT INTO TB_USER (USER_ID, URL) "
        sql += " SELECT NULL, ? "
        sql += " WHERE NOT EXISTS ( SELECT 1 FROM TB_USER WHERE URL = ? )"
        return self.save(sql, url, url)

    def findOrCreateUser(self, url:str):
        sql = " SELECT USER_ID FROM TB_USER WHERE URL = ? "
        value = self.selectOne(sql, url)
        if value is  None or len(value) == 0:
            sql = " INSERT INTO TB_USER VALUES (NULL, ?) "
            self.save(sql, url)
            return self.findOrCreateUser(url)
        else:
            return value[0]
    
    def createUserFollow(self, user_id:int, user_follow_id:int, action:Action = Action.FOLLOWING):
        table_name = "TB_USER_FOLLOWING"
        foreign_key = "USER_FOLLOWING_ID"
        if action != Action.FOLLOWING:
            table_name = "TB_USER_FOLLOWERS"
            foreign_key = "USER_FOLLOWER_ID"
        sql = "  INSERT INTO {} (USER_ID,{}) ".format(table_name, foreign_key)
        sql += " SELECT ?, ? "
        sql += " WHERE NOT EXISTS ( SELECT 1 FROM {} WHERE USER_ID = ? AND {} = ? )".format(table_name, foreign_key)
        return self.save(sql, user_id, user_follow_id, user_id, user_follow_id)

    def createUserPostSource(self, user_id : int, source:str):
        sql = "  INSERT INTO TB_USER_POST (USER_ID, SOURCE ) "
        sql += " SELECT ?, ? "
        sql += " WHERE NOT EXISTS ( SELECT 1 FROM TB_USER_POST WHERE USER_ID = ? AND SOURCE = ? ) "
        self.save(sql, user_id, source, user_id, source)

class BotConnect:

    def __init__(self):
        self.path = "database/bot.db"
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row

    def findBotByName(self, bot_name:str):
        sql = "  SELECT EMAIL, LOGIN, PHONE_NUMBER, PASSWORD FROM TB_BOT_CREDENTIALS "
        sql += " WHERE BOT_NAME = ? "
        conn = self.connection.cursor()
        #https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
        conn.execute(sql, (bot_name,) )
        row = conn.fetchone()
        return tuple(row) if row is not None else row
    
    def availableBots(self):
        sql = " SELECT DESCRIPTION, BOT_NAME FROM TB_BOT_CREDENTIALS "
        return self.connection.cursor().execute(sql).fetchall()
        
    def createBot(self, bot:list):
        sql = " INSERT INTO TB_BOT_CREDENTIALS VALUES ( NULL, "
        sql += " ?, ?, ?, ?, ?, ? )"
        conn = self.connection.cursor()
        conn.execute(sql, bot)
        self.connection.commit()

