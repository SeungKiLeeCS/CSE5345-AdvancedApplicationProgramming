import pymongo
import json
from pymongo import MongoClient as mc

client = mc("mongo smgo7db01.smu.edu:27017 -u seungkil -p hu44kWb5 --authenticationDatabase seungkildb")

member = client["Member"]

print(member.find())