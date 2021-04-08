'''
Author:  Paul Lack
Date created:  4-7-21
Description:  This program uses an API and key available from weatherbit.io
to load relevant weather data to generate graphs in pdf format using the 
numpy and matplotlib libraries.  

This code only supports generating a single pdf file showing the
high temperatures for the next 7 days at this time.

Extra functionality is forthcoming.

I get the data from the API and load it into the appropriate variables
outside of any function because they need to be global variables.

There is currently only one function besides main() that produces a graph
despite the possibility of easily creating more.

Reference the sample data below to inspect the Python dictionary structure
generated from the API's JSON:

{'moonrise_ts': 1617973750, 'wind_cdir': 'SE', 'rh': 80, 'pres': 993.167, 
'high_temp': 8.4, 'sunset_ts': 1618023081, 'ozone': 358.948, 
'moon_phase': 0.0433013, 'wind_gust_spd': 9.79688, 'snow_depth': 3.7, 
'clouds': 99, 'ts': 1617951660, 'sunrise_ts': 1617974908, 
'app_min_temp': -2.6, 'wind_spd': 2.38691, 'pop': 85, 
'wind_cdir_full': 'southeast', 'slp': 1020.12, 'moon_phase_lunation': 0.93, 
valid_date': '2021-04-09', 'app_max_temp': 8.4, 'vis': 14.583, 'dewpt': 0.8, 
now': 1.5, 'uv': 1.91256, 'weather': {'icon': 'r01d', 'code': 500, 
'description': 'Light rain'}, 'wind_dir': 143, 'max_dhi': None, 
'clouds_hi': 51, 'precip': 5.9375, 'low_temp': -0.6, 'max_temp': 8.7, 
'moonset_ts': 1618014300, 'datetime': '2021-04-09', 'temp': 4.2, 
'min_temp': 1.6, 'clouds_mid': 77, 'clouds_low': 94}, 
'''

# import required libraries
import json
import requests
import numpy as np
import matplotlib.pyplot as plt

# put your api token from you free account to weatherbit.io here.
api_token = 'PUT YOUR TOKEN HERE'

# use weatherbit.io documentation to find the correct url base to put 
# here.  This will probably work for you.
api_url_base = 'http://api.weatherbit.io/v2.0/'

# prompts users to enter a city and state
city = input("Enter a city name:  ")
state = input("Enter a two letter state abbreviation:  ")

# creates a request and assigns it to a variable
response = requests.get(api_url_base + 'forecast/daily?city=' + city + ',' \
    + state + '&key=' + api_token) 

weather_dict = json.loads(response.text)

'''
Code for experimentation

# assigns the contents of the json response to a variable
weather_dict = json.loads(response.text)
	# finds the value of the key 'high_temp' that is within the list 'data' that 
    #is within the dictionary 'weather_dict' and assigns it to a variable.
temp_c_today = (weather_dict.get('data')[0].get('high_temp'))
    # converts celsius to fahrenheit
temp_f_today = round(((9/5)*temp_c_today)+32)
    # same as two lines above except it uses the second item in the list.
temp_c_tomorrow = (weather_dict.get('data')[1].get('high_temp'))
    # converts celsius to fahrenheit
temp_f_tomorrow = round(((9/5)*temp_c_tomorrow)+32)
'''

# creates the necessary list variables to hold the data from the API
forecast_high_temp = []
forecast_low_temp = []
forecast_clouds = []
date = []
visibility = []
rain = []
moonset = []
moonrise = []
sunset = []
sunrise = []
wind_gust_speed = []
moon_illumination = []

# uses a for loop to load each of the list variables with 7 consecutive days
# worth of data.
for i in range(7):
	forecast_high_temp.append(weather_dict.get('data')[i].get('high_temp'))
	forecast_low_temp.append(weather_dict.get('data')[i].get('low_temp'))	
	forecast_clouds.append(weather_dict.get('data')[i].get('clouds'))	
	date.append(weather_dict.get('data')[i].get('valid_date'))	
	visibility.append(weather_dict.get('data')[i].get('vis'))
	rain.append(weather_dict.get('data')[i].get('precip'))
	moonset.append(weather_dict.get('data')[i].get('moonset_ts'))
	moonrise.append(weather_dict.get('data')[i].get('moonrise_ts'))	
	sunset.append(weather_dict.get('data')[i].get('sunset_ts'))
	sunrise.append(weather_dict.get('data')[i].get('sunrise_ts'))
	wind_gust_speed.append(weather_dict.get('data')[i].get('wind_gust_spd'))
	moon_illumination.append(weather_dict.get('data')[i].get('moon_phase_lunation'))

# function to generate a pdf file to the specified my chosen location.
def graph_high_temp():
    	
    N = 7
    ind = np.arange(N)	   
    width = 0.35 
    y_pos = np.arange(N)
    p1 = plt.bar(ind, forecast_high_temp, width, color='royalblue', alpha=0.7)
    plt.ylabel("Temp Degrees Celsius")
    plt.title(f"Next 7 Day's High Temperatures for {city}, {state}")
    plt.xticks(ind, date)
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    plt.yticks(np.arange(0, 31, 5))
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.show() 
    plt.savefig(f"/Users/paullack/Python/Seven-Day-Highs-{city}-{state}.pdf")

# main function
def main():
    graph_high_temp()
    print(date[i][5:])	

main()
