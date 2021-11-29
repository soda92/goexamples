import requests
import json
url = "http://localhost:8080/decode"
payload = {"firstname": "John", "lastname": "Doe", "age": 25}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.text)
