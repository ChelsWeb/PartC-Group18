from flask import Blueprint, render_template
from flask import flash, redirect, url_for, session
from db_connector import get_users_collection

# my_account blueprint definition
my_account = Blueprint('my_account', __name__, static_folder='static', static_url_path='/my_account', template_folder='templates')


# Routes
@my_account.route('/my_account')
def index():
    if 'logged_in' not in session or not session['logged_in']:
        flash('Please log in to view my account.', 'error')  # 'error' is an optional category
        return redirect(url_for('login_bp.login'))
    email = session.get('email')  # Assuming you store the user's email in session upon login
    users_collection = get_users_collection()
    user = users_collection.find_one({"email": email})

    if user:
        return render_template('my_account.html', user=user)
    else:
        return "User not found", 404

