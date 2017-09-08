import quandl
import  matplotlib.pyplot as plt
import pandas as pd
import datetime

allcodes = pd.read_csv('LSEcodes.csv')
quandl.ApiConfig.api_key = 'M-T8uDzgVxm-4kEKc3cu'

today = datetime.date.today()
oneyago=today+datetime.timedelta(days=-364)

# for item in allcodes['LSE/DAILY_TRADES']:
#     data = quandl.get(item, column_index='1')
#     prices = data.reset_index()
#     currentprice = prices['Price'].tail(1)
#     oneyearagoprice = prices['Price'][prices['Date']==oneyago]
#
#     if oneyearagoprice>currentprice:
#         print (item)


data = quandl.get('LSE/OPM', column_index='1')
# prices = data.reset_index()
print(data.at['Date'[0],'Price'])
