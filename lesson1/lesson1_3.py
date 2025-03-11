from flask import Flask

app:Flask = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello world!</h1>"

@app.route("/test")
def test():
    return "<h1>こんにちは　世界!</h1>"

@app.route("/user/<user_name>")     #「<>」で囲むと変数として使用できる
def user(user_name):
    return f"<h1>ようこそ{user_name}さん</h1>"


if __name__ == "__main__":
    app.run()