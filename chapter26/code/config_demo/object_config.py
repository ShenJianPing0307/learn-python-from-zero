from flask import Flask


app = Flask(__name__)

# 类的路径
app.config.from_object("config_file.object_base_config.ProConfig")

@app.route("/index")
def index():
    return ""

if __name__ == '__main__':
    app.run()