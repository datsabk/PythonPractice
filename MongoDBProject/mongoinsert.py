import pymongo
from pymongo import MongoClient

myClient = MongoClient()
myDb = myClient.abk
users = myDb.users
users.drop()
users = myDb.users
user1 = {"username":"nick","password":"myverysecurepwd","favourite_number":"445","hobbies":["python","java","webdevelopment"]}
user_id = users.insert_one(user1).inserted_id
print(user_id)
user1 = {"username":"ABK","password":"myverysecurepwd","favourite_number":"545","hobbies":["python","java","webdevelopment"]}
user_id = users.insert_one(user1).inserted_id
print(user_id)

multipleUsers = [{"username":"third","password":"12345"},{"username":"red","password":"blue"}]
inserted = users.insert_many(multipleUsers)
print(inserted.inserted_ids)
print(users.find().count())