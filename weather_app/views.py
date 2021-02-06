from django.shortcuts import render
from django.http.response import HttpResponse
import requests

# Create your views here.
def index(request):
    city_name= 'London'
    url= 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'.format(
        city_name=city_name, key='107f0bb3a6f90f8c582bfa6d95eda8da'
    )

    response=requests.get(url)
    print(response)
    print(response.json())
    myjson=response.json()
    info_dict={
        'city':myjson.get('name'),
        'temp':myjson.get('main').get('temp'),
    }
    
    return render(request,"main/index.html",{"result":info_dict})

