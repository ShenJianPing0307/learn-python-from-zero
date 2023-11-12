from flask import Flask

app = Flask(__name__)

@app.route('/index',strict_slashes=False) #访问http://127.0.0.1:5000/index 或http://127.0.0.1:5000/index/  均可
def index():
    return 'index'


@app.route('/home',strict_slashes=True) #只能访问 http://127.0.0.1:5000/home
def home():
    return 'home'

if __name__ == '__main__':
    app.run()