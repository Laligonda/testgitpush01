import pymongo
client = pymongo.MongoClient("mongodb+srv://dbBHK:Dsa123@cluster0.9eygmye.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Bhaskar",
    "email": "abc@gmail.com"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)