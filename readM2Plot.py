# coding=utf-8
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import calendar
import datetime
import time

import matplotlib.pyplot as plt


excelFile = r'2014M2.xls'
df = pd.read_excel(excelFile)


x = [];
for i in range(3,57):
    x.append(df.loc[4][i])

y=[];
# for col in range(61):
#     if col%2 ==1:
#         y.append(df.loc[7][col])

y =  [[df.loc[row][col+1] for col in range(2,56)] for row in range(6,12,2)];


# plt.figure()
# plt.plot(x,y,'o-')
# plt.legend()
# plt.show()

plt.figure()
for i in range(3):
    plt.plot(x,y[i],'o-',label=str(i))
    plt.legend()
plt.show()
