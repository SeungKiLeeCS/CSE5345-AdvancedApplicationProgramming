import pymongo
import json
from pymongo import MongoClient

client = MongoClient("mongodb://seungkil:hu44kWb5@smgo7db01.smu.edu:27017/")

db = client['seungkildb']
# member = db["Member"]

# member.find({'name': "Hirate Yurina"})

print(client.list_database_names())