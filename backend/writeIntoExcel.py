import random
import time
import pandas as pd
import requests
import re
from openpyxl.workbook import Workbook

urlInfo = []
fakeHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77',
    'Cookie': ''
}  # 伪装浏览器用的请求头


def write(cont, col1, col2, name):
    key = list(cont.keys())
    value = list(cont.values())

    # 利用pandas模块先建立DateFrame类型，然后将两个上面的list存进去
    result_excel = pd.DataFrame()
    result_excel[col1] = key
    result_excel[col2] = value
    # 写入excel
    result_excel.to_excel(name)


def setCookie():
    response = requests.get('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml')
    cookie_value = ''
    for key, value in response.cookies.items():
        cookie_value += key + '=' + value + ';'
    fakeHeaders['Cookie'] = cookie_value


# 链接获取
def getUrlInfo():
    r = requests.get('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml', headers=fakeHeaders)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    temp = r.text

    pattern = 'href=\".*\.shtml\"'
    infoTmp = re.findall(pattern, temp)

    for i in infoTmp:
        urlInfo.append('http://www.nhc.gov.cn' + i[6:len(i) - 1])

    print(urlInfo)


# 页面信息获取
def getPageInfo(url):
    r = requests.get(url, headers=fakeHeaders)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    temp = r.text

    # 获取日期信息 <div class="tit">截至9月6日24时新型冠状病毒肺炎疫情最新情况</div>
    pattern = '<div class="tit">.+</div>'
    s = re.findall(pattern, temp)[0]
    today_is = s[s.index('截至') + 2: s.index('日') + 1]

    # 获取所有段落内容
    pattern = '<p style="text-align: justify; line-height: 1.5; text-indent: 2em; font-family: 仿宋,仿宋_GB2312; ' \
              'font-size: 16pt; -ms-text-justify: inter-ideograph;">.+</p>'
    pInfo = re.findall(pattern, temp)

    i = 0
    # i mean: 0 新增详细， 1 治愈详细， 2 境外输入详细，3 累计确诊详细， 4 无症状新增详细， 5 解除无症状感染者详细，6 港澳台详细

    # 1.
    # 统计中国大陆每日本土新增确诊人数及新增无症状感染人数，境外输入类型和疑似病例等无需统计。
    # 2.
    # 统计所有省份包括港澳台每日本土新增确诊人数及新增无症状感染人数，境外输入类型和疑似病例等无需统计。

    # 数据暂存
    data = {}

    # 新增确诊
    pattern = '本土病例<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">\d+</span>'
    s = re.findall(pattern, pInfo[0])[0]  # 第一个
    data["新增确诊"] = s[s.index('">') + 2:s.index('</span>')]

    # 新增无症状
    pattern = '本土<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">\d+</span>'
    s = re.findall(pattern, pInfo[4])[0]  # 第一个
    data["新增无症状"] = s[s.index('">') + 2:s.index('</span>')]

    write(data, '新增类型', '新增数量', '中国大陆' + today_is + '疫情情况.xlsx')

    # (港澳台外)所有省份新增确诊
    data1 = {}
    pattern = '本土病例<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]*</span>例（.+），'
    s1 = re.findall(pattern, pInfo[0])[0]
    s2 = re.findall('[\u4E00-\u9FA5]+<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]+</span>例', s1)
    for i in range(1, len(s2)):
        data1[s2[i][0:s2[i].index('<span')]] = s2[i][s2[i].index('\">') + 2: s2[i].index('</span>')]
    write(data1, '省份', '新增确诊数量', '各省份' + today_is + '新增确诊.xlsx')
    print(data1)

    # (港澳台外)所有省份新增无症状
    data2 = {}
    pattern = '本土<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]*</span>例（.+）'
    s1 = re.findall(pattern, pInfo[4])[0]
    s2 = re.findall('[\u4E00-\u9FA5]+<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]+</span>例', s1)
    for i in range(1, len(s2)):
        data2[s2[i][0:s2[i].index('<span')]] = s2[i][s2[i].index('\">') + 2: s2[i].index('</span>')]
    write(data2, '省份', '新增无症状数量', '各省份' + today_is + '新增无症状.xlsx')

    # 港澳台信息
    # 香港
    data3 = {}
    pattern = '香港特别行政区<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]*</span>例'
    s = re.findall(pattern, pInfo[6])[0]
    data3["香港累计确诊"] = s[s.index('\">') + 2:s.index('</span>')]
    # 澳门
    pattern = '澳门特别行政区<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]+</span>例'
    s = re.findall(pattern, pInfo[6])[0]
    data3["澳门累计确诊"] = s[s.index('">') + 2:s.index('</span>')]
    # 台湾
    pattern = '台湾地区<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]+</span>例'
    s = re.findall(pattern, pInfo[6])[0]
    data3["台湾累计确诊"] = s[s.index('">') + 2:s.index('</span>')]

    write(data3, '省份', '疫情情况', '港澳台' + today_is + '疫情情况.xlsx')


if __name__ == "__main__":
    # cnt = 0
    # # 获取URL
    # while cnt < 1:
    #     setCookie()
    #     try:
    #         getUrlInfo()
    #         time.sleep(random.randint(0, 5))
    #         cnt += 1
    #     except:
    #         print("false...")
    #         time.sleep(random.randint(0, 5))
    #
    # cnt = 0
    # # 获取当天数据
    # while cnt < 1:
    #     setCookie()
    #     try:
    #         getPageInfo(urlInfo[0])
    #         time.sleep(random.randint(0, 5))
    #         cnt += 1
    #     except:
    #         print("false...")
    #         time.sleep(random.randint(0, 5))

    getPageInfo('http://www.nhc.gov.cn/xcs/yqtb/202209/b9867ea1be624141b41f461a431239d7.shtml')
