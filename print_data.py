import pymongo
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
database_name  = "mydatabase"
collection_name = "mycollection"
db = mongo_client[database_name]
collection = db[collection_name]
# insert one record
one_record = {"name":"David","age":28,"city":"Chicago"}
inserted_one = collection.insert_one(one_record)
print("Inserted one Record ID :",inserted_one.inserted_id)
# insert many record
many_records  = [{"name":"Ella","age":22,"city":"Miami"},
                 {"name":"Frank","age":40,"city":"seatttle"}
]
inserted_many = collection.insert_many(many_records)
print("Inserted Many Records IDs:",inserted_many.inserted_ids)
print("Inserted Records :")
for record in collection.find():
    print(record)
print("One inserted data")
one_inserted_records = collection.find_one({"name":"David"})
print(one_inserted_records)