from flask import Flask, views

app = Flask(__name__)


class IndexView(views.MethodView):
    methods = ['GET']

    def get(self):
        return "get"

    def post(self):
        return "post"


app.add_url_rule('/index', view_func=IndexView.as_view(name="index"))

if __name__ == '__main__':
    app.run()
