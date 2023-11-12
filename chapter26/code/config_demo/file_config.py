from flask import Flask


app = Flask(__name__)

app.config.from_pyfile("config_file/base_config.py")

@app.route("/index")
def index():
    return ""

if __name__ == '__main__':
    app.run()