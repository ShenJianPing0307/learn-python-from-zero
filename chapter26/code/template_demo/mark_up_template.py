from flask import Flask, render_template, Markup

app = Flask(__name__)


def html():
    html_str = Markup("<a href='#'>点击我</a>")
    return html_str


@app.route('/')
def index():
    return render_template('index.html', func=html)


if __name__ == '__main__':
    app.run()