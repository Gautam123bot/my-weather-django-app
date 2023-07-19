from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import urllib

# Create your views here.
import json

def home(request):
    # return render(request, "index.html")
    
    if request.method == 'POST':
        city = request.POST['city']
        city = city.replace(" ", "%20")
        url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=74e217958057438ccafbd16684b6bb10').read()
        w_dict = json.loads(url)

        data = {
            "country_code" : str(w_dict['sys']['country']),
            "coordinate" : str(w_dict['coord']['lon']) + ', ' + str(w_dict['coord']['lat']),
            "temp" : str(w_dict['main']['temp']-273.15) + ' °c',
            "pressure" : str(w_dict['main']['pressure']),
            "humidity" : str(w_dict['main']['humidity']),
            "main" : str(w_dict['weather'][0]['main']),     # 0 given because weather is given as a list and inside that they is dictionary
            "description" : str(w_dict['weather'][0]['description']),   # we are taking dictionary from list 0 so [0] is given
            "icon" : w_dict['weather'][0]['icon'],
            "city_name" : w_dict['name'],
        }
        print(data)
    else:
        data = {}

    return render(request, "index.html", data)