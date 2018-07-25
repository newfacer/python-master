# coding=utf-8
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import calendar
import datetime
import time

import matplotlib.pyplot as plt


excelFile = r'2016AggEconomy.xls'
df = pd.read_excel(excelFile)


x = [];
for i in range(8,74):
    x.append(df.loc[i][0])

# for row in range(0,6):
#     for col in range(0,8):
#         y[row][col]=df.loc[8+row][1+col]

y =  [[df.loc[8+row][1+col] for row in range(66)] for col in range(8)];

plt.figure()
for i in range(8):
    plt.plot(x,y[i],'o-',label=str(i))
    plt.legend()
plt.show()

