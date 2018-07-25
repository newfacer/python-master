# coding=utf-8
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import calendar
import datetime
import time
import os
import sys
from array import array

import matplotlib.pyplot as plt


# excelFile = r'2015Debt.xls'
# df = pd.read_excel(excelFile)

csv_files = [r'2015Debt.xls',r'2016Debt.xls',r'2017Debt.xls',r'2018Debt.xls']
dfs = [pd.read_excel(csv_file) for csv_file in csv_files]


x = [];
for j in range(4):
    for i in range(1,13):
        tmp = dfs[0].loc[5][i]
        if j >0:
           tmp = tmp[:3]+str(j+5)+tmp[4:]
        x.append(tmp)

y=[];
# for col in range(61):
#     if col%2 ==1:
#         y.append(df.loc[7][col])

# for row in range(4):
#     for col in range(12):
#         y.append(dfs[row].loc[28][col+1])


y = [[dfs[row].loc[28][col+1] for col in range(12)] for row in range(4)];
y = np.array(y, dtype = float)
y = np.nan_to_num(y)
y = y.flatten()

# plt.figure()
# plt.plot(x,y,'o-')
# plt.legend()
# plt.show()

plt.figure()
for i in range(1):
    plt.plot(x,y,'o-',label=str(i))
    plt.legend()
plt.show()
