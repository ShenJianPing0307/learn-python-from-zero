"""
作者增、删、改、查
"""

from flask import Blueprint
from flask import render_template

author = Blueprint('author', __name__)


@author.route('/add')
def add():
    return render_template('author/home.html')
