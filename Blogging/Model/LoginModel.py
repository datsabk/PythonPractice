import pymongo
from pymongo import MongoClient
import bcrypt

class LoginModel:

    def __init__(self):
        self.client=MongoClient()
        self.db = self.client.abkmvc
        self.Users= self.db.users

    def check_user(self, data):
        myuser = self.Users.find_one({"username": data.username})
        if bcrypt.checkpw(data.password.encode(), myuser["password"]):
            return myuser["username"]
        else:
            return "error"
