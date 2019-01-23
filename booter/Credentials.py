"""
Class to use as Credentials for SignIn at the site
"""
class Credentials:
    def __init__(self, email:str, username:str, phone_number:str,  password:str):
        self.email = email
        self.username = username
        self.phone_number = phone_number
        self.password = password

