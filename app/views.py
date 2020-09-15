from django.shortcuts import render
import  requests
import  json
from django.views.generic import View


# Create your views here.
#
# city= eval(input("enter a city name:"))
#
# url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=6f07ddc114fc1213eca9097fb580ba8b'.format(city)
#
# res= requests.get(url)
#
# data= res.json()
#
# print(data)
#
class WeatherDetails(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        city = request.POST.get('c1')

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=6f07ddc114fc1213eca9097fb580ba8b'.format(city)


        res = requests.get(url)

        details = res.json()
        print(details)
        temp=details['main']['temp_max']
        pressure=details['main']['pressure']
        humidity=details['main']['humidity']
        speed=details['wind']['speed']
        name=details['name']
        contex={"temp":temp,"pressure":pressure,"humidity":humidity,"speed":speed,"name":name}
        return render(request, "index.html", {"data": contex})