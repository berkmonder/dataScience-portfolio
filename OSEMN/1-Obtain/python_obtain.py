import requests
from bs4 import BeautifulSoup

def getAndParseURL(url):
    """
    Requests url and turns is into a soup object.
    """
    headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup # add .prettify() at the end if you only want to view it


import pymongo

def connectToMongoDB(mongo_username, mongo_password):
    client = pymongo.MongoClient(f"mongodb+srv://{mongo_username}:{mongo_password}@cluster0.d4ojg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    print(client.list_database_names())
    input_db = input("Database Name: ")
    db = getattr(client, input_db)

    print(db.list_collection_names())
    input_collection = input("Collection Name: ")
    collection = getattr(db, input_collection)

    return collection

if __name__ == '__main__':
    url = "https://example.com"
    print(getAndParseURL(url))
    # collection = connectToMongoDB(mongo_username, mongo_password)