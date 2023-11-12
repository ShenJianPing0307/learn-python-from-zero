from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return ({'a': 1, 'b': 2})  # 或者 return jsonify(a='1',b='2')


if __name__ == '__main__':
    app.run()