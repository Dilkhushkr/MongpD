import pymongo
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
database_name  = "mydatabase"
collection_name = "mycollection"
db = mongo_client[database_name]
collection = db[collection_name]
sample_data = [{"name":"Alice","age":30,"city":"new York"},
               {"name":"Bob","age":25,"ciyt":"san Fransico"},
               {"name":"Charlie","age":35,"city":"Los Angeles"}
               ]
collection.insert_many(sample_data)
print("DataBase collection created successfully")