"""
书籍增、删、改、查
"""
from flask import Blueprint
from flask import render_template

books = Blueprint('books', __name__)


@books.route('/home')
def home():
    return render_template('books/home.html')