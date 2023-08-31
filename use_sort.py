import pymongo
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
database_name  = "mydatabase"
collection_name = "mycollection"
db = mongo_client[database_name]
collection = db[collection_name]
asecnding_sort_query = {}
asecnding_sorted_documents = collection.find().sort("age",1)
print("Doucument sorted by age in ascending order:")
for document in asecnding_sorted_documents :
    print(document)
descending_sort_query = {}
descending_sort_documents = collection.find().sort("age",-1)
print("Document sorted by age in descending  order:")
for document in descending_sort_documents:
    print(document)