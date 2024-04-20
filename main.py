import pymongo

# Establishing connection to MongoDB, add your data here, standart port 27017
mongo_client = pymongo.MongoClient("mongodb://login:pass#@ip:port/?authMechanism=DEFAULT")
mongo_db = mongo_client["yourdb"]
your_collection = mongo_db["your_name"]

# Getting all documents from the collection, add your collection name in DB
all_documents = your_collection.find()

# Path to the file to save the data, add your file for save
file_path = "your_data.txt"

# Opening the file for writing
with open(file_path, "w") as file:
    # Writing each document to the file
    for document in all_documents:
        # Forming the string in the required format
        line = f"{document['login']},{document['login']},{document['password']},{document['host']}:{document['port']}\n"
        # Writing the string to the file
        file.write(line)

print("Data successfully exported to file in the specified format:", file_path)
