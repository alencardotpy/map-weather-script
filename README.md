# Map Weather Script
A simple python script to call API from OpenWeather.org and retrive current weather data.

# How it works?
  A simple script will run and do the work of sorting the information that will return by default the following itens:
  - Current temperature.
  - Minimal current temprature.
  - Maximal current temprature.
  - Pressure.
  - Humidity.
  - Feels like temperature.
  - Weather conditions and its representative icons displayed as code and descriptions text(See https://openweathermap.org/weather-conditions).
 
# Requirements
  - Python 3.6+
  - Free or paid API Key that you can get at https://openweathermap.org/

  # Units

    Units of measurement. standard, metric and imperial units are available.   

    By default units will be displayed as 'metric', and it can be changed by editing 'map_wether.py' 
    lines 12 and 50 on 'call_url' variable parameter 'units=metric':

    call_url = ('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city_name, self.api_key))
  

    
   # Getting current weather by City Name

      import map_weather as mw

      foo = '{api key'} #Your API Key

      call_api = mw.CurrentWeather(foo)

      city_weather = call_api.by_city('Sorocaba') #Just informe the city name

      print (city_weather)

      Output:

      {'temp': 32, 'temp_min': 32, 'temp_max': 32, 'pressure': 1010, 'humidity': 35, 'feels_like': 31.65, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}


   # Getting current weather by City ID

      import map_weather as mw

      foo = '{api key'} #Your API Key

      call_api = mw.CurrentWeather(foo)

      city_weather = call_api.by_cityid('3447399')

      print (city_weather)

      Output:

      {'temp': 32, 'temp_min': 32, 'temp_max': 32, 'pressure': 1010, 'humidity': 35, 'feels_like': 31.65, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]}
      
      P.S For City ID, please consult OpenWeatherMap API Docs(https://openweathermap.org/current)

   # Did you liked it or Found a bug?
    - Request features and more functionalities.
    - Suggest code improvements.
    - Report bugs.
    - Collab and help to make it better for everybody.
   
