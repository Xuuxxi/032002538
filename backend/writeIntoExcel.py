# import pandas as pd
# import requests
# import re
# from openpyxl.workbook import Workbook
# import MyFunction
#
#
# def write(cont, col1, col2, name):
#     key = list(cont.keys())
#     value = list(cont.values())
#
#     # 利用pandas模块先建立DateFrame类型，然后将两个上面的list存进去
#     result_excel = pd.DataFrame()
#     result_excel[col1] = key
#     result_excel[col2] = value
#     # 写入excel
#     result_excel.to_excel(name)
#
#     write(data3, '省份', '疫情情况', '港澳台' + today_is + '疫情情况.xlsx')
#
#
# if __name__ == "__main__":