import pymongo
from pymongo import MongoClient

#Connect to database
cluster = MongoClient("YOUR CLUSTER LINK")
db = cluster["test"]
collection = db["test"]

#cleans the db
collection.delete_many({})


def populateDb (name, comment, link, counter,score):
    collection.insert_one({"_id": counter, "name": name,
                           "comment": comment, "profile": link, "score": score})

    return


