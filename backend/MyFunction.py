import requests
import re
import asyncio
import getHtml

urlInfo = []


# 链接获取
def getUrlInfo():
    temp = getHtml.get('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml')

    pattern = 'href=\".*\.shtml\"'
    infoTmp = re.findall(pattern, temp)

    for i in infoTmp:
        urlInfo.append('http://www.nhc.gov.cn' + i[6:len(i) - 1])

    print(urlInfo)


# 页面信息获取
def getPageInfo(url, flag):
    temp = getHtml.get(url)

    # 获取日期信息 <div class="tit">截至9月6日24时新型冠状病毒肺炎疫情最新情况</div>
    pattern = '<div class="tit">.+</div>'
    s = re.findall(pattern, temp)[0]
    today_is = s[s.index('截至') + 2: s.index('日') + 1]

    # 获取所有段落内容
    pattern = '<p style="text-align: justify; line-height: 1.5; text-indent: 2em; font-family: 仿宋,仿宋_GB2312; ' \
              'font-size: 16pt; -ms-text-justify: inter-ideograph;">.+</p>'
    pInfo = re.findall(pattern, temp)

    # mean: 0 新增详细， 1 治愈详细， 2 境外输入详细，3 累计确诊详细， 4 无症状新增详细， 5 解除无症状感染者详细，6 港澳台详细

    # 新增确诊 -> 0
    data0 = {}
    pattern = '本土病例<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">\d+</span>'
    s = re.findall(pattern, pInfo[0])[0]  # 第一个
    data0["新增确诊"] = s[s.index('">') + 2:s.index('</span>')]
    if flag == 0:
        return data0

    # 新增无症状 -> 1
    data1 = {}
    pattern = '本土<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">\d+</span>'
    s = re.findall(pattern, pInfo[4])[0]  # 第一个
    data1["新增无症状"] = s[s.index('">') + 2:s.index('</span>')]
    if flag == 1:
        return data1

    # (港澳台外)所有省份新增确诊 -> 2
    data2 = {}
    pattern = '本土病例<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]*</span>例（.+），'
    s1 = re.findall(pattern, pInfo[0])[0]
    s2 = re.findall('[\u4E00-\u9FA5]+<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]+</span>例', s1)
    for i in range(1, len(s2)):
        data2[s2[i][0:s2[i].index('<span')]] = s2[i][s2[i].index('\">') + 2: s2[i].index('</span>')]
    if flag == 2:
        return data2

    # (港澳台外)所有省份新增无症状 -> 3
    data3 = {}
    pattern = '本土<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]*</span>例（.+）'
    s1 = re.findall(pattern, pInfo[4])[0]
    s2 = re.findall('[\u4E00-\u9FA5]+<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]+</span>例', s1)
    for i in range(1, len(s2)):
        data3[s2[i][0:s2[i].index('<span')]] = s2[i][s2[i].index('\">') + 2: s2[i].index('</span>')]
    if flag == 3:
        return data3

    # 港澳台信息 -> 4
    # 香港
    data4 = {}
    pattern = '香港特别行政区<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]*</span>例'
    s = re.findall(pattern, pInfo[6])[0]
    data4["香港累计确诊"] = s[s.index('\">') + 2:s.index('</span>')]
    # 澳门
    pattern = '澳门特别行政区<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]+</span>例'
    s = re.findall(pattern, pInfo[6])[0]
    data4["澳门累计确诊"] = s[s.index('">') + 2:s.index('</span>')]
    # 台湾
    pattern = '台湾地区<span style="font-family: 仿宋,仿宋_GB2312; font-size: 16pt;">[0-9]+</span>例'
    s = re.findall(pattern, pInfo[6])[0]
    data4["台湾累计确诊"] = s[s.index('">') + 2:s.index('</span>')]

    if flag == 4:
        return data4

    return 'input flag first'


# 获取第i天数据，不断尝试直到全部获取
def getOne(i, flag):
    getUrlInfo()
    return getPageInfo(urlInfo[i], flag)

def getWeekInfo(flag):
    getUrlInfo()
    dic = []
    cnt = 0

    for i in range(0,7):
        dic.append(getPageInfo(urlInfo[cnt], flag))
        cnt += 1

    return dic

