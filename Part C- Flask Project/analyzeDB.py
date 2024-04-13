from dotenv import load_dotenv
load_dotenv()
from db_connector import get_db

def analyze_db():
    db = get_db()

    collections = ['Users', 'Posts', 'Favorites', 'Reviews']

    for collection_name in collections:
        print(f"{collection_name} collection:")
        collection = db[collection_name]
        for doc in collection.find():
            print(doc)
        print()


if __name__ == "__main__":
    analyze_db()
