import re

import requests

import getHtml

import json

from datetime import datetime, timedelta

"""
json.dumps(res) dic res -> str res
json.loads(res) str res -> dic res
"""

"""
信息处理部分
"""


# 检查是否在查找范围
def chkCity(city):
    city_list = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南',
                 '四川', '贵州', '云南', '陕西', '甘肃', '青海', '内蒙古', '广西', '西藏', '宁夏', '新疆', '北京', '天津', '上海', '重庆']

    return city_list.count(city)


# 获取关键信息
def getHtmlMainInfo(url):
    t = ''
    temp = getHtml.get(url, 1)
    # 获取日期信息
    pattern = '20[0-9]+-[0-9]+-[0-9]+'
    infoTmp = re.findall(pattern, temp)
    s = infoTmp[2]
    cur_time = (datetime.strptime(s, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')

    # 获取主体
    pattern = '>.*?<'
    tempInfo = re.findall(pattern, temp)
    for i in tempInfo:
        str_t = i[1:-1]
        t += str_t

    t += cur_time
    return t[t.index('页'):]


# 页面信息获取
def getPageInfo(url):
    temp = getHtmlMainInfo(url)

    # 返回json
    data = {
        'curTime': '',
        'newAdd': '',
        'newNull': '',
        'proAdd': '',
        'proNull': '',
        'hkTotal': '',
        'twTotal': '',
        'amTotal': '',
    }

    # 获取日期信息 xxxx-xx-xx
    data['curTime'] = temp[-10:]

    # 新增确诊
    try:
        data['newAdd'] = re.findall('新增确诊病例(.*?)例', temp)[0]
    except:
        data['newAdd'] = '0'

    # 新增无症状
    try:
        data['newNull'] = re.findall('新增无症状感染者(.*?)例', temp)[0]
    except:
        data['newNull'] = '0'

    # (港澳台外)所有省份新增确诊
    try:
        pro_add = re.findall('本土病例.*?（(.*?)）', temp, re.DOTALL)[0]
        pro_add_key = re.findall('([\u4E00-\u9FA5]+?)[0-9]*?例', pro_add)
        pro_add_value = re.findall('[\u4E00-\u9FA5]+?([0-9]*?)例', pro_add)

        pro_add_info = {}
        for i in range(0, len(pro_add_key)):
            if chkCity(pro_add_key[i]) == 1:
                pro_add_info[pro_add_key[i]] = pro_add_value[i]

        data['proAdd'] = json.dumps(pro_add_info)
    except:
        data['proAdd'] = '0'

    # (港澳台外)所有省份新增无症状
    try:
        pro_null = re.findall('本土[0-9]*?例（.*?）', temp, re.DOTALL)[0]
        pro_null_key = re.findall('([\u4E00-\u9FA5]+?)[0-9]*?例', pro_null)
        pro_null_value = re.findall('[\u4E00-\u9FA5]+?([0-9]*?)例', pro_null)

        pro_null_info = {}
        for i in range(0, len(pro_null_key)):
            if chkCity(pro_null_key[i]) == 1:
                pro_null_info[pro_null_key[i]] = pro_null_value[i]

        data['proNull'] = json.dumps(pro_null_info)
    except:
        data['proNull'] = '0'

    # 港澳台信息
    # 香港
    try:
        pattern = '香港特别行政区[0-9]+例'
        s = re.findall(pattern, temp)[0]
        data['hkTotal'] = s[s.index('行政区') + 3:s.index('例')]

    except:
        data['hkTotal'] = '0'

    try:
        # 澳门
        pattern = '澳门特别行政区[0-9]+例'
        s = re.findall(pattern, temp)[0]
        data['amTotal'] = s[s.index('行政区') + 3:s.index('例')]
    except:
        data['amTotal'] = '0'

    try:
        # 台湾
        pattern = '台湾地区[0-9]+例'
        s = re.findall(pattern, temp)[0]
        data['twTotal'] = s[s.index('地区') + 2:s.index('例')]
    except:
        data['twTotal'] = '0'

    return data


# 获取所有疫情信息页面的 url
def getUrlInfo():
    urlInfo = []
    temp = getHtml.get('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml', 1)

    pattern = 'href=\".*\.shtml\"'
    infoTmp = re.findall(pattern, temp)
    for i in infoTmp:
        urlInfo.append('http://www.nhc.gov.cn' + i[6:len(i) - 1])

    for i in range(2, 40):
        t = getHtml.get('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_' + str(i) + '.shtml', 1)
        pattern = 'href=\".*\.shtml\"'
        tInfo = re.findall(pattern, t)
        for j in tInfo:
            urlInfo.append('http://www.nhc.gov.cn' + j[6:len(j) - 1])

    return urlInfo


# 获取疫苗页面url
def getMedUrlInfo():
    urlInfo = []
    temp = getHtml.get('http://www.nhc.gov.cn/xcs/yqjzqk/list_gzbd.shtml', 2)

    pattern = 'href=\".*\.shtml\"'
    infoTmp = re.findall(pattern, temp)
    for i in infoTmp:
        urlInfo.append('http://www.nhc.gov.cn' + i[6:len(i) - 1])

    for i in range(2, 24):
        t = getHtml.get('http://www.nhc.gov.cn/xcs/yqjzqk/list_gzbd_' + str(i) + '.shtml', 1)
        pattern = 'href=\".*\.shtml\"'
        tInfo = re.findall(pattern, t)
        for j in tInfo:
            urlInfo.append('http://www.nhc.gov.cn' + j[6:len(j) - 1])

    return urlInfo


# 更新最近的 url
def updUrlInfo():
    # 每日新增更新
    medUrl = []
    temp = getHtml.get('http://www.nhc.gov.cn/xcs/yqjzqk/list_gzbd.shtml', 2)

    pattern = 'href=\".*\.shtml\"'
    infoTmp = re.findall(pattern, temp)
    for i in infoTmp:
        medUrl.append('http://www.nhc.gov.cn' + i[6:len(i) - 1])

    for i in medUrl:
        rs = setJavaUrlInfo(getMedNum(i))
        print(rs)
        if rs == '"False"':
            break

    # dayInfo和url更新
    url = []
    temp = getHtml.get('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml', 1)

    pattern = 'href=\".*\.shtml\"'
    infoTmp = re.findall(pattern, temp)
    for i in infoTmp:
        url.append('http://www.nhc.gov.cn' + i[6:len(i) - 1])

    for i in url:
        data = {
            'curTime': getDayInfo(i),
            'url': i
        }

        rs = setJavaUrlInfo(data)
        print(rs)
        if rs == '"false"':
            return
        rs = setJavaDayInfo(getPageInfo(i))
        print(rs)
        if rs == '"false"':
            return


# 获取网页日期数据
def getDayInfo(url):
    temp = getHtml.get(url, 1)
    pattern = '20[0-9]+-[0-9]+-[0-9]+'
    infoTmp = re.findall(pattern, temp)
    s = infoTmp[2]
    return (datetime.strptime(s, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')


# 获取疫苗确诊病例
def getMedNum(url):
    temp = getHtml.get(url, 2)
    pattern = '20[0-9]+-[0-9]+-[0-9]+'
    infoTmp = re.findall(pattern, temp)
    s = infoTmp[2]
    dayInfo = (datetime.strptime(s, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    rs = re.findall('新冠病毒疫苗.*万剂次', temp)[0]
    medNum = rs[rs.index('疫苗') + 2:-3]
    return {'curTime': medNum, 'url': dayInfo}  # 作为新增内容，这边纯粹是为了少写一个数据库，在实际开发中不可以这样混杂数据存储


# -----------------------------------------------------------------------------------
# 通过 Java 操作数据库

def setJavaUrlInfo(data):
    rs = requests.post('http://localhost:8081/urlInfo/setInfo', json=data)
    return rs.text


def getJavaUrlInfo(data):
    rs = requests.get(str('http://localhost:8081/urlInfo/getInfo?curDay=' + data))
    return rs.text


def setJavaDayInfo(data):
    rs = requests.post('http://localhost:8081/dayInfo/setInfo', json=data)
    return rs.text


def getJavaDayInfo(data):
    rs = requests.get(str('http://localhost:8081/dayInfo/getInfo?curDay=' + data))
    return rs.text


# -----------------------------------------------------------------------------------

# 若数据库无数据则初始化数据
def DATA_INIT():
    url = getUrlInfo()

    for i in url:
        data = {'cur_time': getDayInfo(i), 'url': i}
        setJavaUrlInfo(data)
        setJavaDayInfo(getPageInfo(i))