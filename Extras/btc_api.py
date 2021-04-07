#!/usr/bin/python3
"""Paul Lack | Bitcoin Price Tracker - USD
Tracking price of BTC to USD via:
	https://api.coindesk.com/v1/bpi/currentprice.json"""

# import requests to capture HTTP GETs and capture 200 responsis
import requests
#import json

def main():

    api = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    #get the API data and set to variable.  Send a request.
    r = requests.get(api)

    # strip the JSON off the 200 response object and map to new variable
    btcdata = r.json()

    time = btcdata.get("time").get("updated")
    value = btcdata.get("bpi").get("USD").get("rate")

    #open a file we can write to without having to open an close the file
    with open("btcPrice.data", "a") as btc:
    	print(time, file=btc)  # easy way to put info in a file
    	print(value, file=btc)
    	# btc.write()  # another method of putting info in a file

# append data to a file (current time stamp and BTC to USD price from captured data)

# close file

# test area
    print(value)

main()