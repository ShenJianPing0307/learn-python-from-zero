from flask import Flask

application = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')

from .views.author import author
from .views.books import books

# 将所有的蓝图注册到app
application.register_blueprint(author, url_prefix='/author')
application.register_blueprint(books, url_prefix='/books')
