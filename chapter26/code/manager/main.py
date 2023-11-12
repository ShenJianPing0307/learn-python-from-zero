from flask import Flask, render_template

app = Flask(__name__)

stu_list = [
    {"id": 1, "name": "zhangsan", "age": 15},
    {"id": 2, "name": "lisi", "age": 13},
]


@app.route("/list")
def list():
    return render_template("list.html", data=stu_list)

if __name__ == '__main__':
    app.run()