# coding=utf-8
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import calendar
import datetime
import time

import matplotlib.pyplot as plt


excelFile = r'2016all.xls'
df = pd.read_excel(excelFile)


x = [];
for i in range(61):
    if i%2 ==1:
        x.append(df.loc[3][i])

y=[];
# for col in range(61):
#     if col%2 ==1:
#         y.append(df.loc[7][col])

y =  [[df.loc[7+row][col+1] for col in range(0,60,2)] for row in range(0,16,2)];


# plt.figure()
# plt.plot(x,y,'o-')
# plt.legend()
# plt.show()

plt.figure()
for i in range(8):
    plt.plot(x,y[i],'o-',label=str(i))
    plt.legend()
plt.show()
