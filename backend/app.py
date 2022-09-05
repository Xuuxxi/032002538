from flask import Flask, jsonify
import requests
import re

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    data = {
        "msg": "welcome"
    }

    return jsonify(data)


@app.route('/info1')
def getInfo1():
    try:
        getWebInfo('https://pintia.cn/problem-sets/14/problems/type/6')
    except:
        print('gg')

    return 'hello'


def getWebInfo(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/89.0.4389.82 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = 'utf-8'
    temp = r.text

    pattern = '<span class="title-content-title">(.*?)</span>'  # 正则匹配查询内容
    data_list = re.findall(pattern, temp)

    # 去除多余字符
    print(data_list)
    return 0


if __name__ == '__main__':
    app.run()
