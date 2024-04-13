from flask import Blueprint, render_template, session
from db_connector import get_db
import bson
from flask import flash, redirect, url_for

# favorites blueprint definition
favorites = Blueprint(
    'favorites',
    __name__,
    static_folder='static',
    static_url_path='/favorites',
    template_folder='templates'
)

sample_post = {'category': 'Jackets',
                   'location': 'Tel Aviv',
                   'image_filename': 'jacket.png',
                   'price': '100₪',
                   'like_filename': 'liked.png'}
# Routes
@favorites.route('/favorites')
def index():
    if 'logged_in' not in session or not session['logged_in']:
        flash('Please log in to view favorites.', 'error')  # 'error' is an optional category
        return redirect(url_for('login_bp.login'))


    favorites_list = [sample_post]
    return render_template('favorites.html', favorites=favorites_list)
