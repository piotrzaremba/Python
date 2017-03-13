import requests
import json

#http://www.jarloo.com/real-time-google-stock-api/

response = requests.get("http://finance.google.com/finance/info?client=ig&q=NASDAQ%3Afnma", headers={'Connection':'close'})

data = response.text.replace("// [", "")
data = data.replace("]", "")
json_data = json.loads(data)

print (json.dumps(json_data, indent=4, sort_keys=True))

print("Last Price : " + json_data["l"])