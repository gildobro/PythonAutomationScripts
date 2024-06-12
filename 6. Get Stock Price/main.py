import requests
from datetime import datetime
import os
import time


ticker = input("Enter the ticker symbol: ")
from_date = input("Enter start date in yyyy/mm/dd format: ")
to_date = input("Enter emd date in yyyy/mm/dd format: ")

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')


epoch_from = time.mktime(from_datetime.timetuple())
epoch_to = time.mktime(to_datetime.timetuple())


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={int(epoch_from)}&period2={int(epoch_to)}&interval=1d&events=history&includeAdjustedClose=true" 


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content
print(epoch_from, ' ', epoch_to)


#define a directory folder
directory = r'C:\Users\GilDobrovinsky\OneDrive - Cypfer\Desktop\Courses and Notes\Python Automation Course\Get Stock Price\prices'
file_path = os.path.join(directory, f'{ticker}.csv')

#create the directory if it does not exist
os.makedirs(directory, exist_ok=True)

with open(file_path, 'wb') as file:
    file.write(content)