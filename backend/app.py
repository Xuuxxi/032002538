import asyncio

from flask import Flask, jsonify, request

import MyFunction

app = Flask(__name__)

dic = []


@app.route('/')
def hello_world():  # put application's code here
    data = {
        "msg": "welcome"
    }

    return jsonify(data)


@app.route('/getInfo', methods=["GET"])
def getInfo():
    cnt = 0
    flag = 0
    if request.method == "GET":
        cnt = request.args.get("cnt")
        flag = request.args.get("flag")

    return MyFunction.getWeekInfo(flag)


if __name__ == '__main__':
    app.run()
