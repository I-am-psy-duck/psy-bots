from booter.Bot import Bot, Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from booter.Connection import Connection
from booter.bot_connection import findByXpath
import random
import time
from booter.bot_util import getChromeDriver, convertElementTextToInt


class InstagramAction:

    def __init__(self, bot: Bot, connection:Connection):
        self.profile = webdriver.ChromeOptions()
        self.profile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

        # selenium does not open a window
        self.profile.add_argument("--headless")
        
        self.browser = webdriver.Chrome(str(getChromeDriver()), chrome_options=self.profile)
        self.connection = connection
        self.bot = bot

    def _followList(self, user:str, action:Action, max:int = -1 ):

        print("Going to: {}".format(self.bot.urls.get(action.name) + user))
        time.sleep(1)
        self.browser.get(self.bot.urls.get(action.name) + user)
        time.sleep(1.5)

        """
            Loads all the XPATH ELEMENTS
        """
        user_xpath_button = findByXpath(self.bot, action, self.connection, 1)
        user_xpath_modal  = findByXpath(self.bot, action, self.connection, 2)
        user_xpath_number = findByXpath(self.bot, action, self.connection, 3)
        user_xpath_scroll = findByXpath(self.bot, action, self.connection, 4)
        user_xpath_dinamic_li_elements = findByXpath(self.bot, action, self.connection, 5)

        # it tries to convert, if returns an error, 10000 is setted
        follow_count = convertElementTextToInt(self.browser.find_element_by_xpath(user_xpath_number).text)
        time.sleep(1)

        print("Total user {}: {}".format(action.name, follow_count))
        # It find the button
        user_follow_button = self.browser.find_element_by_xpath(user_xpath_button)
        time.sleep(1)

        # clicks to the button and waits to the modal open
        user_follow_button.click()
        time.sleep(3)

        # gets the modal
        follow_list = self.browser.find_element_by_xpath(user_xpath_modal)

        # this is a dinamic element
        li_elements_list = self.browser.find_element_by_xpath(user_xpath_dinamic_li_elements)
      
        # find the scroll 
        scroll = self.browser.find_element_by_xpath(user_xpath_scroll)

        # scroll utility
        actionChain = webdriver.ActionChains(self.browser)

        # Gets the default length of followers of the modal
        default_size = len(li_elements_list.find_elements_by_css_selector('li'))


        # if was setted a max users
        if max is None:
            max = -1
        error = False
        while ( default_size < follow_count and max == -1) or ( max > ( default_size + 12 ) ) :
            try:
                time.sleep(2)
                actionChain.send_keys_to_element(scroll, Keys.SPACE).perform()
                time.sleep(2)
                default_size = len(li_elements_list.find_elements_by_css_selector('li')) 
            except Exception as e:
                print('Error: {}'.format(e))
                error = True
                break
        print("Total: {}".format(default_size))

        # List to return the users
        users = []

        if error is not True:
            for user in li_elements_list.find_elements_by_css_selector('li'):
                user_link = str(user.find_element_by_css_selector('a').get_attribute('href'))
                users.append(user_link) 
                if len(users) >= default_size:
                    break
        else:
            print("Not possible to extract")
            return users

        print("Finished extracting {} users . . .".format(default_size))        
        return users


    def login(self):
        # go to URL, we use ENUM
        self.browser.get(self.bot.urls.get(Action.LOGIN.name))
        time.sleep(1)

        # Get the XPATH CONTENT
        xpath_username = findByXpath(self.bot, Action.LOGIN, self.connection, 1)
        xpath_password = findByXpath(self.bot, Action.LOGIN, self.connection, 2)

        # set the username on username element
        self.browser.find_element_by_xpath(xpath_username).send_keys(self.bot.credentials.username)
        time.sleep(1.5)

        # set the pass on password element
        self.browser.find_element_by_xpath(xpath_password).send_keys(self.bot.credentials.password)
        time.sleep(1)

        #press the button
        self.browser.find_element_by_xpath(xpath_password).send_keys(Keys.ENTER)
        time.sleep(3)

    def followUser(self, user:str):
        
        print("Going to: {}".format(self.bot.urls.get(Action.FOLLOW.name) + user))
        self.browser.get(self.bot.urls.get(Action.FOLLOW.name) + user)
        time.sleep(1)

        # get the xpath element to follow the user
        follow_user_xpath = findByXpath(self.bot, Action.FOLLOW, self.connection)
        follow_button = self.browser.find_element_by_xpath(follow_user_xpath)
        time.sleep(2)
        follow_button.click()
        time.sleep(2)
        

    def getUserFollowing(self, user:str, max:int = None):
        return self._followList(user, Action.FOLLOWING, max)

    def getFollowingUser(self, user:str, max : int = None):
        return self._followList(user, Action.FOLLOWERS, max)
        
    def likeUserPhoto(self, user:str, comments:list = None, max:int = None):

        print("Going to: {}".format(self.bot.urls.get(Action.LIKE.value) + user))
        self.browser.get(self.bot.urls.get(Action.LIKE.value) + user)
        time.sleep(1.5)

        post_total_xpath = findByXpath(self.bot, Action.LIKE, self.connection, 1)
        first_post_xpath = findByXpath(self.bot, Action.LIKE, self.connection, 2)
        like_post_xpath = findByXpath(self.bot, Action.LIKE, self.connection, 3)
        next_post_xpath = findByXpath(self.bot, Action.LIKE, self.connection, 4)
        comment_post_xpath = findByXpath(self.bot, Action.LIKE, self.connection, 5)

        posts_total = self.browser.find_element_by_xpath(post_total_xpath) 

        # gets the total of posts of the user
        TOTAL = convertElementTextToInt(posts_total.text)

        print("Total posts:{}".format(TOTAL))
        if TOTAL == 0:
            print("User: {} has no posts!".format(user))
        else:

            if max is not None:
                TOTAL = max if max <= TOTAL else ( TOTAL - 1)   


            # criar outro xpath para usuários que não tem histórias 
            #first_post = self.browser.find_element_by_xpath(first_post_xpath)
            first_post = self.browser.find_elements_by_class_name("_9AhH0")[0]

            time.sleep(2)
            #open the post
            first_post.click()        
            time.sleep(5)

            liked = 0
            while liked < ( TOTAL - 1 ) :
                like_button = self.browser.find_element_by_xpath(like_post_xpath)
                time.sleep(2)
                like_button.click()

                if comments is not None and len(comments) > 0:
                    # if user want to use comments
                    comment = comments[random.randint(0, len(comments) - 1)]
                    self.browser.find_element_by_xpath(comment_post_xpath).clear()
                    self.browser.find_element_by_xpath(comment_post_xpath).click()
                    time.sleep(1)
                    self.browser.find_element_by_xpath(comment_post_xpath).send_keys(comment)
                    self.browser.find_element_by_xpath(comment_post_xpath).send_keys(Keys.ENTER)
                    time.sleep(1.5)

                next_button = self.browser.find_element_by_xpath(next_post_xpath)
                time.sleep(1)
                next_button.click()
                time.sleep(2)
                liked += 1
            print("Finished with: {} posts liked".format(liked))

    def seeUserStories(self, user:str, comment:str):
        pass


    def close(self, msg:str = None):
        if msg is not None:
            print("Closing browser due to exception: {}".format(msg))
        else:
            print("Closing browers...")
        self.browser.close()

    def downloadPhotos(self, user:str):

        print("Going to: {}".format(self.bot.urls.get(Action.DOWNLOAD.value) + user))
        self.browser.get(self.bot.urls.get(Action.DOWNLOAD.value) + user)
        time.sleep(1.5)

        post_total_xpath = findByXpath(self.bot, Action.DOWNLOAD, self.connection, 1)

        posts_total = self.browser.find_element_by_xpath(post_total_xpath) 
       
        ## scroll element
        scroll = self.browser.find_element_by_tag_name("html")

        #total posts
        total = convertElementTextToInt(posts_total.text)
        
        print("Total posts:{}".format(total))

        # the first 25 posts 
        images = self.browser.find_elements_by_tag_name("img")
        sources = []
       
        # add the sources to the list
        for i in images:
            sources.append(i.get_attribute("src"))

        # while we do not get all the posts
        while total > len(sources):
            # scroll down
            scroll.send_keys(Keys.END)
            time.sleep(2)
            images = self.browser.find_elements_by_tag_name("img")
            
            #append the sources to the list
            for i in images:
                sources.append(i.get_attribute("src"))
            # remove repeated values
            sources = list(set(sources))

        print("Success getting images sources... total: {}".format(len(sources)))
        return sources


