
from flask import Blueprint, render_template, request, redirect, url_for, flash
from db_connector import get_users_collection
from datetime import datetime

registration = Blueprint('registration', __name__, static_folder='static', static_url_path='/registration',
                         template_folder='templates')


@registration.route('/registration', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        location = request.form.get('city')
        gender = 'female' if 'female' in request.form else 'male' if 'male' in request.form else None

        users_collection = get_users_collection()


        if users_collection.find_one({"email": email}):
            flash('Email already registered.', 'error')
            return redirect(url_for('registration.index'))


        users_collection.insert_one({
            "username": username,
            "email": email,
            "password_hash": password,
            "joined_date": datetime.utcnow(),
            "location": location,
            "gender": gender
        })

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login_bp.login'))

    return render_template('registration.html')

@registration.route('/registration', methods=['GET'])
def show_registration_form():
    return render_template('registration.html')
