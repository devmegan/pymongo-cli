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
    print("5: Exit (q)")

    option = input("Enter option: ")
    return option


def menu_loop():
    while True:
        option = show_menu()

        if option == "1":
            print("\nOption 1 selected")
            # todo: add_record()
        elif option == "2":
            print("\nOption 2 selected")
            get_record()
        elif option == "3":
            print("\nOption 3 selected")
            #todo: edit_record()
        elif option == "4":
            print("\nOption 4 selected")
            delete_record()
        elif option == "5" or option == "q":
            print("\nClosing Connection to MongoDB...")
            connection.close()
            print("Connection closed")
            break
        else:
            print("\nError! Option " + option  + " invalid")


# CRUD FUNCTIONS
def get_record():
    print("---")

    first = input("Enter first name > ")
    last = input("Enter last name > ")

    print("\nSearching for a record of: {} {}".format(first, last))

    doc = None

    try:
        doc = collelection.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("\nError fetching record")

    if not doc:
        print("\nNo records found matching: {} {}.".format(first, last))

    return doc


def delete_record():
    print("\nSearch for record to delete:")

    doc = get_record()

    if not doc:
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        confirmation = input("\nIs this the record you want to delete? (Y/N) > ")

        if confirmation.lower() == 'y':
            try:
                collection.delete_one(doc)
                print("Record deleted!")
            except:
                print("Error deleting the record")


# ESTABLISH CONNECTION AND SHOW MENU
connection = mongo_connect(MONGO_URI)
collection = get_collection(connection, DB_NAME, COLLECTION_NAME)

menu_loop()
