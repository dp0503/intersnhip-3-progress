import requests

response = requests.get('https://fakestoreapi.com/products/')

mydata = response.json()

for i in mydata:
    print("my name is ",i['title'])
