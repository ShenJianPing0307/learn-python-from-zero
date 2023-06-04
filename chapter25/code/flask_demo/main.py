from flask import Flask

# 实例化Flask对象
app = Flask(__name__)


@app.route('/')
def index():
    return "index"



if __name__ == '__main__':
    app.run()
