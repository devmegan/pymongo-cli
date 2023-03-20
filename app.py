import os
import pymongo
from dotenv import load_dotenv

load_dotenv()
load_dotenv('.env.local', override=True)

MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = os.environ.get('DB_NAME')
COLLECTION_NAME = os.environ.get('COLLECTION_NAME')


def mongo_connect(url):
    print("Establishing connection to MongoDB...")

    if not url:
        print("MONGO_URI value missing")
        exit()

    try:
        connection = pymongo.MongoClient(url)
        print("Connected!")
        return connection
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)


def get_collection(connection, db_name, collection_name):
    if not connection:
        print("Connection to MongoDB lost. Restart app.")
        exit()
    elif not db_name or not collection_name:
        print("Make sure DB_NAME and COLL_NAME set in .env")
        exit()

    collection = connection[db_name][collection_name]
    print("---\nCollection: " + str(collection) + "\n---")
    return collection


def show_menu():
    print("")
    print("1: Add a record")
    print("2: Find a record")
    print("3: Edit a record")
    print("4: Delete a record")
    print("5: Exit")

    option = input("Enter option: ")
    return option


connection = mongo_connect(MONGO_URI)
collection = get_collection(connection, DB_NAME, COLLECTION_NAME)

show_menu()