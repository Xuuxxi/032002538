import re

import getHtml

def getMedNum():
    rs = re.findall('新冠病毒疫苗.*万剂次',getHtml.get('http://www.nhc.gov.cn/jkj/s7915/202209/16d333a68d7c4f3ea16df247f213b5f8.shtml',2))[0]
    return rs[rs.index('疫苗') + 2:-3]