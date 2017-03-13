#http://www.otcmarkets.com/reports/symbol_info.csv

import requests
import json

url = 'http://www.otcmarkets.com/reports/symbol_info.csv'

response = requests.get(url, headers={'Connection':'close'})

for line in response.text.split('\r\n'):
     print(line)