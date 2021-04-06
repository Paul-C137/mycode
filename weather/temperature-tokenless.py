# import required libraries
import json
import requests
# put your api token from you free account to weatherbit.io here.
api_token = 'YOUR OWN TOKEN HERE'
# use weatherbit.io documentation to find the correct url base to put here.  
#This will probably work for you.
api_url_base = 'http://api.weatherbit.io/v2.0/'
# enter your own city and state 
city = 'Sedro-Woolley'
state = 'WA'
# creates a request and assigns it to a variable
response = requests.get(api_url_base + 'forecast/daily?city=' + city + ',' \
+ state + '&key=' + api_token) 
#response = requests.get('https://google.com')
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
# prints the current day's expected high temperature.
print('The high temperature today will be ' + str(temp_f_today) +' degrees fahrenheit.')
# prints tomorrows expected high temperature.
print('The high temperature tomorrow will be ' + str(temp_f_tomorrow) +' degrees fahrenheit.')