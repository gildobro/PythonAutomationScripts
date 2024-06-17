import requests

def get_weather(city, api_key='4e8168637ec4d034b671a65824370a5f', units='metric'):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    weather_lists = content['list']
    weather_city = content['city']['name']

    path = r'C:\Users\GilDobrovinsky\OneDrive - Cypfer\Desktop\Courses and Notes\Python Automation Course\10. Weather Forecast API Exercise\data.txt'

    for weather_list in weather_lists:
        with open(path, 'a') as file:
            file.write(f"{weather_city}, {weather_list['dt_txt']}, {weather_list['main']['temp']}, {weather_list['weather'][0]['description']}\n")
    return



print(get_weather(city="Jerusalem"))