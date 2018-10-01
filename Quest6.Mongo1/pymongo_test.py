import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://seungkil:hu44kWb5@smgo7db01.smu.edu:27017/seungkildb')
db = client.seungkildb

players = [ 
    {
        "name": "Mesut Ozil",
        "age": 29,
        "position": "AM"
    }, {
        "name": "Aaron Ramsey",
        "age": 27,
        "position": "CM"
    }, {
        "name": "Pierre-Emerick Aubameyang",
        "age": 28,
        "position": "ST"
    }, {
        "name": "Laurent Koscielny",
        "age": 31,
        "position": "CB"
    }, {
        "name": "Alexandre Lacazette",
        "age": 27,
        "position": "ST"
    }
]


for p in players:
        db.player.insert(p)

for p in db.player.find():
        print(p)




# From pre-defined db

# find by key
# print( db.Member.find({"name": "Hirate Yurina"}) )

# print( db.Actress.findall() )