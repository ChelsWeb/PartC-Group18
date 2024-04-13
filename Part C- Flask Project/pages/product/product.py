from flask import Blueprint, render_template

explore = Blueprint('product', __name__, static_folder='static', template_folder='templates')

@explore.route('/product')
def index():
    return render_template('product.html')