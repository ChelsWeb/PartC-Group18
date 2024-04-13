

from flask import render_template, Blueprint, request, session, redirect, url_for, flash, current_app
from pymongo import MongoClient
from db_connector import get_users_collection
from flask import flash




login_bp = Blueprint(
    'login_bp',
    __name__,
    static_folder='static',
    static_url_path='/login',
    template_folder='templates'
)



@login_bp.route('/', methods=['GET', 'POST'])
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in') == True:
        return redirect('/explore')

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        users_collection = get_users_collection()
        user = users_collection.find_one({"email": email, "password_hash": password})

        if user:
            session['email'] = email
            session['logged_in'] = True
            return redirect('/explore')
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')


users_collection = MongoClient()["mydatabase"]["Users"]


def authenticate_user(email, password):
    user = users_collection.find_one({"email": email, "password_hash": password})
    if user:
        return True
    return False