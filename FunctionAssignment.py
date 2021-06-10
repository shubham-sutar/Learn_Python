'''''
class Function:
   def __init__(self,num):
       self.num=num

if (num%2):
    print("num is even")
else:
    print("num is odd")

h1=Function(25)
print(h1.num)
'''''
"""
# defining the function having the one parameter as input
def evenOdd(n):

    #if remainder is 0 then num is even
    if(n==0):
        return True

    #if remainder is 1 then num is odd
    elif(n==1):
        return False
    else:
        return evenOdd(n-2)

# Input by geeks
num=6
if(evenOdd(num)):
    print(num,"num is even")
else:
    print(num,"num is odd")
"""


# defining the function having
# the one parameter as input
def evenOdd(n):
    # if remainder is 0 then num is even
    if (n % 2 == 0):
        return True

    # if remainder is 1 then num is odd
    elif (n % 2 != 0):
        return False
    else:
        return evenOdd(n)

'''
# Input by geeks
num = 3
if (evenOdd(num)):
    print(num, "num is even")
else:
    print(num, "num is odd")
'''

"""
def evenOdd(n):
    # if remainder is 0 then num is even
    if (n % 2 == 0):
        return True

    # if remainder is 1 then num is odd
    elif (n % 2 != 0):
        return False
    else:
        return evenOdd(n)
"""

"""
# Input by geeks
num = 3
if (evenOdd(num)):
    print(num, "num is even")
else:
    print(num, "num is odd")
"""
"""
from sklearn import tree

features = [[2,100],[6,25],[1,300],[1,1000],[4,100],[10,100]]
label = [1,2,1,1,2,2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,label)
print(clf.predict([[4,140]]))
"""

import pandas as pd
import numpy as np
import yfinance
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [12, 7]
plt.rc('font', size=14)

name = 'TSLA'
ticker = yfinance.Ticker(name)
df = ticker.history(interval="1d", start="2021-03-15", end="2021-06-04")
df['Date'] = pd.to_datetime(df.index)
df['Date'] = df['Date'].apply(mpl_dates.date2num)
df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
print(df)


def isSupport(df, i):
    support = df['Low'][i] < df['Low'][i - 1] and df['Low'][i] < df['Low'][i +
                                                                           1] and df['Low'][i + 1] < df['Low'][
                  i + 2] and df['Low'][i - 1] < df['Low'][i - 2]
    return support


def isResistance(df, i):
    resistance = df['High'][i] > df['High'][i - 1] and df['High'][i] > df['High'][i +
                                                                                  1] and df['High'][i + 1] > df['High'][
                     i + 2] and df['High'][i - 1] > df['High'][i - 2]
    return resistance


levels = []
for i in range(2, df.shape[0] - 2):
    if isSupport(df, i):
        levels.append((i, df['Low'][i]))
    elif isResistance(df, i):
        levels.append((i, df['High'][i]))


        def plot_all():
            fig, ax = plt.subplots()

    candlestick_ohlc(ax, df.values, width=0.6, \
                     colorup='green', colordown='red', alpha=0.8)
    date_format = mpl_dates.DateFormatter('%d %b %Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    fig.tight_layout()
    for level in levels:
        plt.hlines(level[1], xmin=df['Date'][level[0]], \
                   xmax=max(df['Date']), colors='blue')
    fig.show()

    plot_all()