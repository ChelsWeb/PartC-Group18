from flask import Flask, request, render_template, session, redirect, url_for

###### App setup
app = Flask(__name__)
app.secret_key='123'
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.explore.explore import explore

app.register_blueprint(explore)

## About
from pages.favorites.favorites import favorites

app.register_blueprint(favorites)

## Profile
from pages.seller.seller import seller

app.register_blueprint(seller)

## login
from pages.login.login import login_bp

app.register_blueprint(login_bp)

## my_account
from pages.my_account.my_account import my_account

app.register_blueprint(my_account)

## registration
from pages.registration.registration import registration

app.register_blueprint(registration)

## upload product
from pages.UploadProduct.uploadproduct import uploadproduct

app.register_blueprint(uploadproduct)


## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers

app.register_blueprint(page_error_handlers)

###### Components
## Main login
from components.main_menu.main_menu import main_menu

app.register_blueprint(main_menu)

##Logout
@app.route('/logout', methods = ['GET'])
def logout():
    session['logged_in']=False
    session['email']=''
    return redirect(url_for('login_bp.login'))


##DataBase

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from db_connector import *
from dotenv import load_dotenv
load_dotenv()
from db_connector import get_users_collection



def create_users():
    users_collection = get_users_collection()



def create_database():
    db = cluster["mydatabase"]
    print("Database created successfully!")


mydatabase = cluster['2Fashionable']
users_collection = mydatabase['Users']
posts_collection = mydatabase['Posts']
favorites_collection = mydatabase['Favorites']
reviews_collection = mydatabase['Reviews']

users = [
{
    "username": "johndoe",
    "email": "john@example.com",
    "password_hash": "johndoe",
    "joined_date": "2024-01-01",
    "location": "Tel Aviv"},
{
  "username": "alexsmith",
  "email": "alex@example.com",
  "password_hash": "alex",
  "joined_date": "2024-03-10",
  "location": "Haifa"},

{
  "username": "mikebrown",
  "email": "mike@example.com",
  "password_hash": "mike",
  "joined_date": "2024-04-05",
  "location": "Eilat"},
{
  "username": "sarahgreen",
  "email": "sarah@example.com",
  "password_hash": "sarah",
  "joined_date": "2024-05-20",
  "location": "Netanya"},
{
  "username": "danielred",
  "email": "daniel@example.com",
  "password_hash": "daniel",
  "joined_date": "2024-06-15",
  "location": "Beersheba"
},
{
  "username": "danielred",
  "email": "chelsea@example.com",
  "password_hash": "chelsea",
  "joined_date": "2024-06-15",
  "location": "Beersheba"
}
]
users_collection.insert_many(users)

posts = [
    {"title": "Summer Dress", "description": "Light and breezy, perfect for summer days.", "category": "Dresses", "price": 50, "posted_by": "johndoe", "posted_date": "2024-03-10", "status": "active"},
    {"title": "Retro Sneakers", "description": "Vintage vibes, barely worn.", "category": "Shoes", "price": 75, "posted_by": "alexsmith", "posted_date": "2024-03-15", "status": "active"},
    {"title": "Classic Wool Coat", "description": "Elegant and warm, in excellent condition.", "category": "Coats", "price": 150, "posted_by": "mikebrown", "posted_date": "2024-03-20", "status": "active"},
    {"title": "Silk Scarf", "description": "Add a touch of luxury to any outfit.", "category": "Accessories", "price": 40, "posted_by": "sarahgreen", "posted_date": "2024-03-25", "status": "active"}
]

posts_collection.insert_many(posts)

favorites = [
    {"user_id": "johndoe", "post_id": "ObjectId_of_Designer_Denim_Jeans"},
    {"user_id": "alexsmith", "post_id": "ObjectId_of_Vintage_Leather_Jacket"},
    {"user_id": "mikebrown", "post_id": "ObjectId_of_Summer_Dress"},
    {"user_id": "sarahgreen", "post_id": "ObjectId_of_Retro_Sneakers"}
]
favorites_collection.insert_many(favorites)

reviews = [
    {"reviewer_id": "alexsmith", "seller_id": "johndoe", "item_id": "ObjectId_of_Summer_Dress", "rating": 5, "comment": "Absolutely love the dress!", "review_date": "2024-04-01"},
    {"reviewer_id": "johndoe", "seller_id": "alexsmith", "item_id": "ObjectId_of_Retro_Sneakers", "rating": 5, "comment": "These sneakers are just what I was looking for. Great condition!", "review_date": "2024-04-05"},
    {"reviewer_id": "sarahgreen", "seller_id": "mikebrown", "item_id": "ObjectId_of_Classic_Wool_Coat", "rating": 4, "comment": "The coat is warm and stylish. Fast shipping!", "review_date": "2024-04-10"},
    {"reviewer_id": "mikebrown", "seller_id": "sarahgreen", "item_id": "ObjectId_of_Silk_Scarf", "rating": 5, "comment": "The scarf adds a perfect touch to my outfits. Love it!", "review_date": "2024-04-15"}
]
reviews_collection.insert_many(reviews)





