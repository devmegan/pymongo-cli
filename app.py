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


connection = mongo_connect(MONGO_URI)
