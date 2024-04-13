import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# get your uri from .env file
uri = os.environ.get('DB_URI')

# create cluster and database instances
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['2Fashionable']  # Access your database



def get_users_collection():
    return mydatabase['Users']

def get_db():
    return mydatabase
