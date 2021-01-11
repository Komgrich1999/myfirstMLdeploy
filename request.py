
import requests

url = 'http://localhost:5000/results'
obj = {
    'Gender' : 0,
    'Age' : 64,
    'Payment Method' : 3,
    'LastTransaction' : 98.0
}
r = requests.post(url,json=obj)
rr = requests.get(url)

print(r.json())