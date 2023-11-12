from flask import Flask
from flask.config import Config

app = Flask(__name__)

# 直接配置
app.config['DEBUG'] = True # 调试模式
app.config['SECRET_KEY'] = "ABCDEFG"

@app.route("/index")
def index():
    return ""

if __name__ == '__main__':
    app.run()