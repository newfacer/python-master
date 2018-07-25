# coding=utf-8
import pandas as pd
import numpy as np
from pyexcel_xls import save_data
from pyexcel_xls import get_data
from datetime import datetime,timedelta
import calendar
import datetime
import time
from numpy import nan as NaN
import numpy

# def gen_dates(b_date, days):
#     day = timedelta(days=1)
#     for i in range(days):
#         yield b_date + day*i

def gen_dates(b_date, days):
    day = 1
    for i in range(days):
        yield b_date + day*i

def get_date_list(start=None, end=None):
    """
    获取日期列表
    :param start: 开始日期
    :param end: 结束日期
    :return:
    """
    if start is None:
        start = datetime.strptime("2000-01-01", "%Y-%m-%d")
    if end is None:
        end = datetime.now()
    data = []
    # for d in gen_dates(start, (end-start).days):
    for d in gen_dates((int)(start), int(end)-int(start)+1):
        data.append(d)
    return data

day_now = '20180101' #给定日期
day_begin = day_now[0:6]+'01' #月初肯定是1号 所以 直接替换 就可以
monthRange = calendar.monthrange(int(day_now[0:3]),int(day_now[4:6]))#得到本月的天数
day_end = day_now[0:6]+str(monthRange[1])
# time_begin = datetime.datetime.strptime(day_begin, "%Y%m%d")
# time_end = datetime.datetime.strptime(day_end, "%Y%m%d")
#date_list = get_date_list(time_begin,time_end)
date_list = get_date_list(day_begin,day_end)

pd.set_option("max_colwidth",1000)
pd.set_option('precision', 3)

pd.set_option('display.expand_frame_repr',False)
pd.set_option("display.colheader_justify",'right')
pd.set_option('display.width', 200)
pd.option_context('display.float_format', lambda x: '%.3f' % x)

# df = get_data(r'test.xls')
# print(df)
# save_data(r'convert.xls', df)

excelFile = r'test.xls'
# df = pd.DataFrame(pd.read_excel(excelFile,sheet_name=[u'现金日记账'],skiprows=[0]),  index=[0])
# df = pd.read_excel(excelFile,sheet_name=[u'现金日记账'],skiprows=[0])
df = pd.read_excel(excelFile,sheet_name=[u'现金日记账'])

df['现金日记账'].values
df['现金日记账'].loc[:,u'贷\u3000方'][2] = 2500.51

local_time = []
for i in range(df['现金日记账'].loc[:,u'日期'].size):
    df['现金日记账'].loc[:,u'日期'][i] = datetime.datetime.strptime(str(date_list[i]), "%Y%m%d").strftime('%Y/%m/%d')
# df.to_excel('convert.xls', sheet_name=u'现金日记账',index=False,header=True)

# for i in range(len(date_list)):
#     df['现金日记账'].loc[:,u'日期'][i] = datetime.datetime.strptime(str(date_list[i]), "%Y%m%d").strftime('%Y/%m/%d')



multilist = [[NaN for col in range(6)] for row in range(len(date_list)-len(df['现金日记账'])) ]

for row in range(len(multilist)):
    multilist[row][0] = datetime.datetime.strptime(str(date_list[len(df['现金日记账'])+row]), "%Y%m%d").strftime('%Y/%m/%d')

df1 = pd.DataFrame(df['现金日记账'] )
df2 = pd.DataFrame(multilist,columns=df1.columns)
writer = pd.ExcelWriter('convert.xls')

# result = pd.concat([df1, series], axis=0, join_axes=[df1._info_axis])
result = pd.concat([df1, df2])
# result = df1._series.append(series)
# df1.loc[:,'贷\u3000方'].astype(float)
result.to_excel(writer,u'现金日记账',index=False,float_format='%.3f')
writer.save()