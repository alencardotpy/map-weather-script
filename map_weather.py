import requests

class CurrentWeather:
    

    def __init__(self, api_key):

        self.api_key = api_key
    
    def by_city(self,city_name):

        call_url = ('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city_name, self.api_key))
        resp = requests.get(call_url).json()
        if len(resp) == 2:
            if resp['cod'] == '401' or resp['cod'] == 401:
                return resp['message']

            elif resp['cod'] == '404' or resp['cod'] == 404:
                return resp['message']

            elif resp['cod'] == '429' or resp['cod'] == 429:
                return resp['message']

            else:

                return resp['message']
        else:
            temp = resp['main']['temp']
            temp_min = resp['main']['temp_min']
            temp_max = resp['main']['temp_max']
            pressure = resp['main']['pressure']
            humidity = resp['main']['humidity']
            feels_like = resp['main']['feels_like']
            weather  = resp['weather']

            bycity_dict = dict()
            bycity_dict['temp'] = temp
            bycity_dict['temp_min'] = temp_min
            bycity_dict['temp_max'] = temp_max
            bycity_dict['pressure'] = pressure
            bycity_dict['humidity'] = humidity
            bycity_dict['feels_like'] = feels_like
            bycity_dict['weather'] = weather
        
            return bycity_dict
    
    def by_cityid(self,city_id):


        call_url = ('http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric'.format(city_id,self.api_key))
        resp = requests.get(call_url).json()

        if len(resp) == 2:
            if resp['cod'] == '401' or resp['cod'] == 401:
                return resp['message']

            elif resp['cod'] == '404' or resp['cod'] == 404:
                return resp['message']

            elif resp['cod'] == '429' or resp['cod'] == 429:
                return resp['message']

            else:

                return resp['message']
        else:
            temp = resp['main']['temp']
            temp_min = resp['main']['temp_min']
            temp_max = resp['main']['temp_max']
            pressure = resp['main']['pressure']
            humidity = resp['main']['humidity']
            feels_like = resp['main']['feels_like']
            weather  = resp['weather']

            bycityid_dict = dict()
            bycityid_dict['temp'] = temp
            bycityid_dict['temp_min'] = temp_min
            bycityid_dict['temp_max'] = temp_max
            bycityid_dict['pressure'] = pressure
            bycityid_dict['humidity'] = humidity
            bycityid_dict['feels_like'] = feels_like
            bycityid_dict['weather'] = weather
        
            return bycityid_dict

#DriverCode
