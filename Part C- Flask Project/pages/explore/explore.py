from flask import Blueprint, render_template
from flask import flash, redirect, url_for

explore = Blueprint(
    'explore',
    __name__,
    static_folder='static',
    template_folder='templates')


@explore.route('/explore')
def index():
    if 'logged_in' not in session or not session['logged_in']:
        flash('Please log in to view explore page.', 'error')  # 'error' is an optional category
        return redirect(url_for('login_bp.login'))
    posts = [
        {'category': 'Shirts', 'location': 'Tel Aviv', 'image_filename': 'Poncho.png', 'price': '20₪', 'like_filename': 'like.png' },
        {'category': 'Jackets', 'location': 'Tel Aviv', 'image_filename': 'jacket.png', 'price': '100₪', 'like_filename': 'liked.png'},
        {'category': 'Jewelery', 'location': 'Jerusalem', 'image_filename': 'earrings.png', 'price': '200₪', 'like_filename': 'like.png' },
        {'category': 'Shirts', 'location': 'Ra\'anana', 'image_filename': 'shirt.png', 'price': '15₪', 'like_filename': 'like.png' },
        {'category': 'Shirts', 'location': 'Rehovot', 'image_filename': 'shirt2.png', 'price': '15₪', 'like_filename': 'like.png' },
        {'category': 'Sweatshirts', 'location': 'Rehovot', 'image_filename': 'sweatshirt.png', 'price': '40₪', 'like_filename': 'like.png' },
        {'category': 'Jackets', 'location': 'Ra\'anana', 'image_filename': 'jeanjacket.png', 'price': '90₪', 'like_filename': 'like.png' },
        {'category': 'Jackets', 'location': 'Tel Aviv', 'image_filename': 'blazer.png', 'price': '120₪', 'like_filename': 'like.png' }
    ]
    return render_template('explore.html', posts=posts)


from flask import jsonify, request, session
from db_connector import get_db
import bson


@explore.route('/toggle-favorite', methods=['POST'])
def toggle_favorite():
    if not session.get('logged_in'):
        return jsonify({'error': 'User not logged in'}), 401

    email = session.get('email')
    data = request.json
    post_id = data['post_id']
    liked = data['liked']

    post_id = bson.ObjectId(post_id)

    db = get_db()
    favorites_collection = db['Favorites']

    if liked:
        # Remove from favorites
        favorites_collection.delete_one({'user_email': email, 'post_id': post_id})
    else:
        # Add to favorites
        favorites_collection.insert_one({'user_email': email, 'post_id': post_id})

    return jsonify({'success': True})