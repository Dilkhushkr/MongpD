import pymongo



if __name__ == "__main__":
    print("Welcome to pyMongo")
    client =  pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['harry']
    collection = db['mysampleCollectionForHarry']
    rec = {"Name":"john"}
    #collection.delete_one(rec)
    up = collection.delete_many(rec)
    print(up.deleted_count)
     