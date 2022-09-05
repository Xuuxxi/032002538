import requests
import re
import sys


# 检查网站编码和编译器编码
def chkEncoding(url):
    print(sys.getdefaultencoding())
    html = requests.get(url)
    print(html.encoding)


def getWebInfo(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    temp = r.text

    pattern = '[0-9]-[0-9]+'  # 正则匹配查询内容
    info1 = re.findall(pattern, temp)
    pattern = '[\u4E00-\u9FA5]+'
    info2 = re.findall(pattern, temp)

    for i in range(0,len(info1)):
        print(info1[i] + " " + info2[i])


if __name__ == "__main__":
    getWebInfo(
        'https://pintia.cn/api/problem-sets/14/problem-list?exam_id=1508611480445493248&problem_type=CODE_COMPLETION&limit=100')
