from datetime import datetime, timedelta

from flask import Flask, jsonify, request
from flask_cors import CORS

import MyFunction

app = Flask(__name__)
cors = CORS(app)


@app.before_first_request
def get_dayInfo():
    MyFunction.updUrlInfo()
    print("init... ")


@app.route('/')
def hello_world():  # put application's code here
    data = {
        "msg": "welcome"
    }
    print('init success,enjoy the website!')
    return jsonify(data)

@app.route('/sub')
def sub_day():
    if request.method == "GET":
        cur_day = request.args.get("curDay")
        res = (datetime.strptime(cur_day, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
        return jsonify({'cul_day': res})



# @app.route('/getDayInfo', methods=["GET"])
# def getDayInfo():
#     tmp = SqlFunction.getAll()
#     dic = {}
#     for i in tmp:
#         dic[i[0]] = i[1]
#     print('getDayInfo... data = ', end='')
#     print(dic)
#     return jsonify(dic)
#
#
# @app.route('/setCnt', methods=["GET"])
# def setCnt():
#     if request.method == "GET":
#         cnt = request.args.get("cnt")
#         SqlFunction.setCnt(cnt)
#         print('setCnt... data = ', end='')
#         return jsonify('OK')
#
#
# @app.route('/getCnt', methods=["GET"])
# def getCnt():
#     data = {'cnt': SqlFunction.getCnt()[1]}
#     print('getCnt... data = ', end='')
#     print(data)
#     return jsonify(data)
#
#
# @app.route('/getInfo', methods=["GET"])
# def getInfo():
#     flag = 0
#     cnt = 0
#     if request.method == "GET":
#         cnt = request.args.get("cnt")
#         flag = request.args.get("flag")
#
#     return jsonify(MyFunction.getOne(cnt, flag))


if __name__ == '__main__':
    app.run()
