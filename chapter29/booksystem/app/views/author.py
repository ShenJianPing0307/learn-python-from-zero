"""
作者增、删、改、查
"""

from flask import Blueprint
from flask import render_template, request, redirect,url_for
from app.utils.init_db import db
from app.migrate.author.operate import all_author_sql, add_author_sql

author = Blueprint('author', __name__)


@author.route('/home')
def home():
    result = db.get_all(all_author_sql)
    print(result)
    return render_template('author/home.html', data=result)


@author.route('/add', methods=["POST"])
def add():
    username = request.form.get("username")
    email = request.form.get("email")
    db.execute(add_author_sql, (username, email))
    return redirect(url_for('author.home'))
