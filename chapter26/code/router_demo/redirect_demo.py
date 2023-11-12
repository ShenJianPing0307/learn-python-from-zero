from flask import Flask

app = Flask(__name__)


@app.route('/v1/index', methods=['GET', 'POST'], endpoint='index1', redirect_to="/v2/index2")
def index():
    return 'index'


@app.route('/v2/index2', methods=['GET', 'POST'], endpoint='index2')
def index2():
    return 'index2'


if __name__ == '__main__':
    app.run()