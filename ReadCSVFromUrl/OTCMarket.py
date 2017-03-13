#http://www.otcmarkets.com/reports/symbol_info.csv

import requests
import json
import sys
import time

from urllib.request import urlopen

url = 'http://www.otcmarkets.com/reports/symbol_info.csv'
csv = urlopen(url)

list = []

for row in csv:
#    if "ZZLL" in row.decode("utf-8"):
     print(row.decode("utf-8"))
     inside = []
     str = row.decode("utf-8")
     inside = str.split(',')
     list.append(inside)

csv.close()

# Lets take the first row off since it consists of column headers.
list.pop(0)

for row in list:
    symbol = row[0].replace("\"", "")
    innerUrl = "http://finance.google.com/finance/info?client=ig&q=NASDAQ%3A" + symbol
    time.sleep(10)
    response = requests.get(innerUrl, headers={'Connection':'close'})
    if response.status_code == 200:
         data = response.text.replace("// [", "")
         data = data.replace("]", "")
         try:
              json_data = json.loads(data)
              print(row[0] + " Last Price : " + json_data["l"])
         except:
              print("Unexpected error:", sys.exc_info()[0])
              continue
    elif response.status_code == 503:
         print("503 Service Unavailable - You propbably hit the request limit and got throttled")