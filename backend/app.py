from flask import Flask, jsonify, request
from flask_cors import CORS

import MyFunction
import SqlFunction

app = Flask(__name__)
cors = CORS(app)


@app.before_first_request
def get_dayInfo():
    SqlFunction.setCnt(0)
    data = MyFunction.getDayInfo()
    if SqlFunction.getOne(0) is None:
        SqlFunction.ins(data)
    else:
        SqlFunction.upd(data)
    print("init... ")


@app.route('/')
def hello_world():  # put application's code here
    data1 = {
        "msg": "welcome"
    }

    return jsonify(data1)


@app.route('/getDayInfo', methods=["GET"])
def getDayInfo():
    tmp = SqlFunction.getAll()
    dic = {}
    for i in tmp:
        dic[i[0]] = i[1]
    print('getDayInfo... data = ', end='')
    print(dic)
    return jsonify(dic)


@app.route('/setCnt', methods=["GET"])
def setCnt():
    if request.method == "GET":
        cnt = request.args.get("cnt")
        SqlFunction.setCnt(cnt)
        print('setCnt... data = ', end='')
        return jsonify('OK')


@app.route('/getCnt', methods=["GET"])
def getCnt():
    data = {'cnt': SqlFunction.getCnt()[1]}
    print('getCnt... data = ', end='')
    print(data)
    return jsonify(data)


@app.route('/getInfo', methods=["GET"])
def getInfo():
    flag = 0
    cnt = 0
    if request.method == "GET":
        cnt = request.args.get("cnt")
        flag = request.args.get("flag")

    return jsonify(MyFunction.getOne(cnt, flag))


if __name__ == '__main__':
    app.run()
