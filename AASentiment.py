import quandl
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd
import datetime
import numpy as np


quandl.ApiConfig.api_key = 'M-T8uDzgVxm-4kEKc3cu'

today = datetime.date.today()

data = quandl.get('AAII/AAII_SENTIMENT')

# for item in list(data.columns.values):
#     print (item)

# Bullish
# Neutral
# Bearish
# Total
# Bullish 8-Week Mov Avg
# Bull-Bear Spread
# Bullish Average
# Bullish Average + St. Dev
# Bullish Average - St. Dev
# S&P 500 Weekly High
# S&P 500 Weekly Low
# S&P 500 Weekly Close

plotdata = data[['Bullish']]
snpdata = data[['S&P 500 Weekly Close']]
plotdata.plot()
snpdata.plot()
plt.show(block=True)



