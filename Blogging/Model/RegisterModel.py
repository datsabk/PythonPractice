import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:

    def __init__(self):
        self.client=MongoClient()
        self.db = self.client.abkmvc
        self.Users= self.db.users

    def insert_user(self, data):
        print("data is ", data)
        hashed = bcrypt.hashpw(data.password.encode(),bcrypt.gensalt())
        id= self.Users.insert({"username": data.username, "name": data.display_name, "password": hashed, "email": data.email})
        myuser = self.Users.find_one({"username":data.username})
        if bcrypt.checkpw("abk1".encode(), myuser["password"]):
            print("matches")
        print(id)
