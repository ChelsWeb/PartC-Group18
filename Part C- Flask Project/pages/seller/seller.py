from flask import Blueprint
from flask import render_template, redirect, url_for


# explore blueprint definition
seller = Blueprint(
    'seller',
    __name__,
    static_folder='static',
    static_url_path='/seller',
    template_folder='templates'
)


# Routes
@seller.route('/seller')
def index():
    return render_template('seller.html')
