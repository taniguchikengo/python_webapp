from flask import Flask

app:Flask = Flask(__name__)     #インスタンスを作成

@app.route("/")                 #ルートにアクセスした時の処理
def index():
    return "<h1>Hello world!</h1>"  #相手のブラウザに対して左記コードを返す

if __name__ == "__main__":
    app.run()