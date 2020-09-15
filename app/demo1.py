import  requests

import  json
from pprint import pprint







city= input("enter a city name:")

url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=6f07ddc114fc1213eca9097fb580ba8b'.format(city)

res= requests.get(url)

data= res.json()

# print(data)
# pprint(data)

temp=data['main']['temp']
print(temp)

