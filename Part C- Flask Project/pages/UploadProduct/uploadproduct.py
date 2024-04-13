from flask import Blueprint, render_template, request, redirect, url_for, flash
from db_connector import get_users_collection
from datetime import datetime

uploadproduct = Blueprint('uploadproduct',
                         __name__,
                         static_folder='static',
                         static_url_path='/uploadproduct',
                         template_folder='templates')


@uploadproduct.route('/uploadproduct')
def index():
    return render_template('UploadProduct.html')
