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
import random


def generate_rand(n, sum_v):
    Vector = [random.random() for i in range(n)]
    Vector = [ int(i / sum(Vector) * sum_v) for i in Vector]
    if sum(Vector) < sum_v:
        Vector[0] += sum_v-sum(Vector)
    return Vector

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
total_fee = [64877,60580,63882,62352,63876,63117,18416,13281]
total_balance = 23042
day_begin = day_now[0:6]+'01' #月初肯定是1号 所以 直接替换 就可以
monthRange = calendar.monthrange(int(day_now[0:3]),int(day_now[4:6]))#得到本月的天数
day_end = day_now[0:6]+str(monthRange[1])
date_list = get_date_list(day_begin,day_end)

pd.set_option("max_colwidth",1000)
pd.set_option('precision', 2)

pd.set_option('display.expand_frame_repr',False)
pd.set_option("display.colheader_justify",'right')
pd.set_option('display.width', 200)
pd.option_context('display.float_format', lambda x: '%.2f' % x)


excelFile = r'test.xls'
df = pd.read_excel(excelFile,sheet_name=[u'现金日记账'])

df['现金日记账'].values
df['现金日记账'].loc[:,u'贷\u3000方'][2] = 2500.51

local_time = []
for i in range(df['现金日记账'].loc[:,u'日期'].size):
    df['现金日记账'].loc[:,u'日期'][i] = datetime.datetime.strptime(str(date_list[i]), "%Y%m%d").strftime('%Y/%m/%d')


total_size = random.randint(5, 8) + 23
# total_size = 28
multilist = [[NaN for col in range(6)] for row in range(total_size) ]
content = ["教职工薪酬", "场地租赁费", "水电费", "幼儿生活用品费", "办公用品费","教课用品费","管理费用","业务活动费用","交通补贴费用","玩具易耗品费用","装修及设备购置费"]  

# multilist[9][0] =datetime.datetime.strptime(str(date_list[9]), "%Y%m%d").strftime('%Y/%m/%d')
multilist[9][0] =date_list[9]
multilist[9][2] =content[0]
multilist[9][4] = 40000
# multilist[14][0] =datetime.datetime.strptime(str(date_list[14]), "%Y%m%d").strftime('%Y/%m/%d')
multilist[14][0] =date_list[14]
multilist[14][2] =content[1]
multilist[14][4] = 11500

# total_life_fee = random.uniform(2300, 2500)
# total_office_fee = random.uniform(2300, 2500)
# total_lecture_fee = random.uniform(1900, 2100)
# total_manage_fee =  random.uniform(1900, 2100)
# total_we_fee = random.uniform(1100, 1400)
# total_other_fee = random.uniform(2500,3000)
# total_decoration_fee = random.uniform(52500, 54000)

fit_condition = True
while fit_condition == True:
    b_count= 0;
    c_count= 0;
    d_count= 0;
    e_count= 0;
    tmp_list = generate_rand(6,total_fee[0]-40000-11500)
    for i in range(6):
        if tmp_list[i] >= 2300 and  tmp_list[i] <= 2500:
            b_count =  b_count + 1
        if tmp_list[i] >= 1900 and  tmp_list[i] < 2100:
            c_count =  c_count + 1
        if tmp_list[i] >= 1100 and  tmp_list[i] <= 1400:
            d_count =  d_count + 1
        if tmp_list[i] > 2500 and  tmp_list[i] <= 3000:
            e_count =  e_count + 1
    if b_count == 2 and c_count == 2 and d_count == 1 and e_count == 1:
        fit_condition = False

# while fit_condition == True:
#     b_count= 0;
#     c_count= 0;
#     d_count= 0;
#     e_count= 0;
#     tmp_list = generate_rand(6,total_fee[1]-40000-11500)
#     for i in range(6):
#         if tmp_list[i] >= 1400 and  tmp_list[i] <= 1600:
#             b_count =  b_count + 1
#         if tmp_list[i] >= 1200 and  tmp_list[i] < 1400:
#             c_count =  c_count + 1
#         if tmp_list[i] >= 900 and  tmp_list[i] < 1200:
#             d_count =  d_count + 1
#         if tmp_list[i] > 1600 and  tmp_list[i] <= 2800:
#             e_count =  e_count + 1
#     if b_count == 2 and c_count == 2 and d_count == 1 and e_count == 1:
#         fit_condition = False

total_life_fee = 0
total_office_fee = 0
total_lecture_fee = 0
total_manage_fee =  0
total_we_fee = 0
total_other_fee = 0
for i in range(6):
    if tmp_list[i] >= 2300 and  tmp_list[i] <= 2500:
        if total_life_fee == 0:
            total_life_fee = tmp_list[i]
        else:
            total_office_fee = tmp_list[i]
    if tmp_list[i] >= 1900 and  tmp_list[i] < 2100:
        if total_lecture_fee == 0:
            total_lecture_fee = tmp_list[i]
        else:
            total_manage_fee = tmp_list[i]
    if tmp_list[i] >= 1100 and  tmp_list[i] <= 1400:
        total_we_fee = tmp_list[i]
    if tmp_list[i] > 2500 and  tmp_list[i] <= 3000:
        total_other_fee =  tmp_list[i]

# for i in range(6):
#     if tmp_list[i] >= 1400 and  tmp_list[i] <= 1600:
#         if total_life_fee == 0:
#             total_life_fee = tmp_list[i]
#         else:
#             total_office_fee = tmp_list[i]
#     if tmp_list[i] >= 1200 and  tmp_list[i] < 1400:
#         if total_lecture_fee == 0:
#             total_lecture_fee = tmp_list[i]
#         else:
#             total_manage_fee = tmp_list[i]
#     if tmp_list[i] >= 900 and  tmp_list[i] < 1200:
#         total_we_fee = tmp_list[i]
#     if tmp_list[i] > 1600 and  tmp_list[i] <= 2800:
#         total_other_fee =  tmp_list[i]


print("total_life_fee is %d" % total_life_fee)  
print("total_office_fee is %d" % total_office_fee)
print("total_lecture_fee is %d" % total_lecture_fee)
print("total_manage_fee is %d" % total_manage_fee)
print("total_we_fee is %d" % total_we_fee)
print("total_other_fee is %d" % total_other_fee)


# multilist[total_size-1][0] =datetime.datetime.strptime(str(date_list[len(date_list)-1]), "%Y%m%d").strftime('%Y/%m/%d')
multilist[total_size-1][0] = date_list[len(date_list)-1]
multilist[total_size-1][2] = content[2]
multilist[total_size-1][4] = total_we_fee

life_list = generate_rand(5,total_life_fee)
office_list = generate_rand(5,total_office_fee)
lecture_list = generate_rand(5,total_lecture_fee)
manage_list = generate_rand(5,total_manage_fee)
other_size = total_size - 23
other_list = generate_rand(other_size,total_other_fee)


tmp_date = date_list[0:total_size-1]
# tmp_date=random.sample(range(date_list[0],date_list[len(date_list)-1]+1),total_size)
# random.shuffle(tmp_date)
tmp_main = ["幼儿生活用品费", "办公用品费","教课用品费","管理费用"]
main_dict = {"幼儿生活用品费":life_list, "办公用品费":office_list, "教课用品费":lecture_list,"管理费用":manage_list}
tmp_other = ["业务活动费用","交通补贴费用","玩具易耗品费用"]
divisor = 0
remainder = 0
for i in range(total_size):
    if i == 9:
       continue
    elif i == 14:
        continue
    elif i == total_size-1:
        continue
    
    if i <9:
        divisor = (i+1)//5
        remainder = (i+1)%5
        if i == 4:
            multilist[i][2] = tmp_other[0]
            multilist[i][4] = other_list[0]
        else:
            multilist[i][2] = tmp_main[remainder-1]
            multilist[i][4] = main_dict[tmp_main[remainder-1]][divisor]
            
    elif i > 9 and i < 14 :
        divisor  = (i+1)//5
        remainder = (i+1)%5
        multilist[i][2] = tmp_main[remainder-1]
        multilist[i][4] = main_dict[tmp_main[remainder-1]][divisor]
    elif i > 14 and i < 17:
        remainder = (i-14)%3
        multilist[i][2] = tmp_other[remainder]
        multilist[i][4] = other_list[1] if remainder == 1 else other_list[2]
    elif i >= 17 and i < 21:
        remainder = (i-16)%5
        multilist[i][2] = tmp_main[remainder-1]
        multilist[i][4] = main_dict[tmp_main[remainder-1]][3]
    elif i >= 21 and i < 23:
        remainder = (i-20)%3
        multilist[i][2] = tmp_other[remainder-1]
        multilist[i][4] = other_list[3] if remainder == 1 else other_list[4]
    elif i >= 23 and i < 27:
        remainder = (i-22)%5
        multilist[i][2] = tmp_main[remainder-1]
        multilist[i][4] = main_dict[tmp_main[remainder-1]][4]
    elif i== 27:
        multilist[i][2] = tmp_other[2]
        multilist[i][4] = other_list[5]
    elif i>27:
        remainder = (i-27)%3
        multilist[i][2] = tmp_other[remainder-1]
        multilist[i][4] = other_list[6] if remainder == 1 else other_list[7]

    # choice_date = random.choice(tmp_date[0:total_size-1])
    multilist[i][0] = tmp_date[i]



temp_arraylist = np.array(multilist)
# multilist =temp_arraylist
multilist =temp_arraylist[np.lexsort(temp_arraylist[:,::-1].T)]
for row in range(len(multilist)):
   multilist[row][0] = datetime.datetime.strptime(str(multilist[row][0]), "%Y%m%d").strftime('%Y/%m/%d')

multilist = multilist.tolist()
for i in range(len(multilist)):
    for j in range(len(multilist[0])):
        if(multilist[i][j]) == 'nan':
           multilist[i][j] = NaN

for i in range(len(multilist)):
    for j in range(len(multilist[0])):
        multilist[i][4]= int(multilist[i][4])
        multilist[i][5] = total_balance - multilist[i][4]
    total_balance = multilist[i][5] 


# for row in range(len(multilist)):
#     multilist[row][0] = datetime.datetime.strptime(str(date_list[row]), "%Y%m%d").strftime('%Y/%m/%d')

df1 = pd.DataFrame(df['现金日记账'] )
df2 = pd.DataFrame(multilist,columns=df1.columns)
writer = pd.ExcelWriter('convert.xls')

result = pd.concat([ df2])
result.to_excel(writer,u'现金日记账',index=False,float_format='%.3f')
writer.save()