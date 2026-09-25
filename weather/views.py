import requests
from django.shortcuts import render
from .models import WeatherData
def weather(request):
        city=request.GET.get('city')
        if not city:
         return render(request, 'weather.html', {
            'error': 'Please enter a city'
        })

        api_key='c2fbd19f1630de315ba936fd81551a47'
        url='https://api.openweathermap.org/data/2.5/weather'
        params={
            'q':city,
            'appid':api_key,
            'units':'metric'
        }
        response=requests.get(url,params=params)
        
        data = response.json()
       
        if response.status_code==200:
            WeatherData.objects.create(
            city=data['name'],
            temperature=data['main']['temp'],
            description=data['weather'][0]['description'],
            humidity=data['main']['humidity']
           
           )
            context = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity']
            }
     
            
        else:
            context={'error':'city not found'}
        return render(request,'weather.html',context)