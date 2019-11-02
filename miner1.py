#Import the time library to be able to run the algorithm for a certain set of time.
import time
import csv
import robin_stocks as r
import  pandas as pd
from datetime import datetime

#Set up robin-stocks api login info
login = r.login('alarconfer12@gmail.com','Mirey12345')
#Variables for common time data_types
minute = 60
hour = (minute * 60)
day = hour * 24
month = day * 30

#Create a end point
end = time.time() + minute

my_crypto_currencies = r.crypto.get_crypto_positions()
crypto_names = [val['currency']['code'] for val in my_crypto_currencies]

crypto_data = pd.DataFrame()
data_str = 'time,name,ask_price,bid_price,mark_price' + '\n'
list_of_data = []
while time.time() < end:
    try:
        for name in range(len(crypto_names)):
            data = {    
                         
                         'name': crypto_names[name],
                         'buy_price': r.crypto.get_crypto_quote(crypto_names[name])['ask_price'],
                         'sell_price': r.crypto.get_crypto_quote(crypto_names[name])['bid_price'],
                         'mark_price': r.crypto.get_crypto_quote(crypto_names[name])['mark_price'],
                         'time': datetime.now()
                    }
            print(data)
            list_of_data.append(data)
            data_str += str(data['time']) + ',' + crypto_names[name] + ',' + r.crypto.get_crypto_quote(crypto_names[name])['bid_price'] + ',' + r.crypto.get_crypto_quote(crypto_names[name])['ask_price'] + ',' + r.crypto.get_crypto_quote(crypto_names[name])['mark_price']  + '\n'
    except TypeError:
        pass

with open('crypto_data.csv','a') as f:
    f.write(data_str)
print(data_str)
print(1)
df = pd.read_csv('crypto_data.csv',header=0)
df = df[['name','bid_price','ask_price','mark_price']]
print(df)
