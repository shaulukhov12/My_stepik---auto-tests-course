import requests
import json
api_url = 'https://openweathermap.org/data/2.5/weather'

city = input("City?")

params = {
    'q': city,
    'appid': '439d4b804bc8187953eb36d2a8c26a02',
    'units': 'metric'
}
res = requests.get(api_url,params)
#print(res.status_code)
#print(res.headers["Content-Type"])
#print(res.json())

data = res.json()
template = "Current temperature in {} is {}"
#print(data['main']['temp'])
print(template.format(city, data['main']['temp']))