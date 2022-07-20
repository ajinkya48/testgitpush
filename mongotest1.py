import pymongo

client = pymongo.MongoClient("mongodb+srv://ajinkya:ajinkya48@cluster0.81syx.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"aj",
    "mailID":"aj@ineuron.ai",
    "surname":"yadav"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)