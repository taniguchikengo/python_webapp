from flask import Flask

app:Flask = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello world!</h1>"

@app.route("/test")     #「/test」にアクセスした時の処理
def test():
    return "<h1>こんにちは　世界!</h1>"


if __name__ == "__main__":
    app.run()