from flask import Flask

app = Flask(__name__)


def index():
    return ""


app.add_url_rule('/index', view_func=index, methods=['GET', 'POST'], endpoint='index')

if __name__ == '__main__':
    app.run()
