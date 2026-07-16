# Created a weather cli program that uses api calls to get data from 
# api using your city name, and api that i have now hidden.
# in case you want to practice you can use data.json for it.
# or you can sign up to openweather and get you own api key from there
# create a api_key.txt file and paste your api key there, then the program
# should work properly. 

import requests
import sys

try:
    city = input('enter your city name: ')
    with open('api_key.txt', 'r') as f:
        api_key = f.read()

except FileNotFoundError:
    print("the file where api is stored is not present, please create it first and add api to it")
    sys.exit()

try:
    args = {
        'q': city,
        'appid': f'{api_key}',
        'units': 'metric'
    }
    data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=args, timeout=10)
    data.raise_for_status()

except requests.exceptions.Timeout:
    print("Time out. API took more time then expected to get data. Request aborted")
    sys.exit()

except requests.exceptions.HTTPError as http_err:
    status_code = data.status_code
    if status_code == 401:
        print("Error: Invalid API Key. Please check your 'api_key.txt' file.")
    elif status_code == 404:
        print(f"Error: Could not find a city named '{city}'. Check your spelling.")
    else:
        print(f"HTTP Error occurred: {http_err}")
    sys.exit()

except requests.exceptions.RequestException:
    print("Network Error: Failed to connect to the internet or OpenWeather servers.")
    sys.exit()

data = data.json()    
main_data = data['main']
print(main_data)

temperature = main_data['temp']
feels_like = main_data['feels_like']
humidity = main_data['humidity']

print(f"In your City: {city}")
print(f"The temprature is: {temperature} Degree Centigrade")
print(f"Humidity: {humidity}%")
print(f"Feels Like: {feels_like} Degree Centigrade")