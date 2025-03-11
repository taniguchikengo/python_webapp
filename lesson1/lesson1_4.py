from flask import Flask

app:Flask = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello world!</h1>"

@app.route("/test")
def test():
    return "<h1>こんにちは　世界!</h1>"

@app.route("/user/<user_name>")
def user(user_name):
    return f"<h1>ようこそ{user_name}さん</h1>"

@app.route("/user/<user_name>/<int:age>")   #「/」で分けて複数の変数を使用できる
def user2(user_name,age):
    return f"<h1>{user_name}さんは、{age}歳です。</h1>"

if __name__ == "__main__":
    #app.run()
    app.run(host="192.168.10.21",port=8080) #hostにPCのIPアドレスを入れることで他のPC(lan内)からアクセスできるようになる
                                            #portを指定することもできる