
from flask import Blueprint, render_template


main_menu = Blueprint('main_menu', __name__, static_folder='static', static_url_path='/main_menu', template_folder='templates')



@main_menu.route('/explore')
def explore():
    return render_template('explore.html')

@main_menu.route('/favorites')
def favorites():
    return render_template('favorites.html')

@main_menu.route('/login')
def login():
    return render_template('login.html')

@main_menu.route('/registration')
def registration():
    return render_template('registration.html')

@main_menu.route('/my_account')
def my_account():
    return render_template('my_account.html')
