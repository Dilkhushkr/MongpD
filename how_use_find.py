import pymongo
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
database_name  = "mydatabase"
collection_name = "mycollection"
db = mongo_client[database_name]
collection = db[collection_name]
query = {"age":{"$gt":25}}
matching_documents = collection.find(query)
print("Documents with age greater than 25:")
for document in matching_documents:
    print(document)