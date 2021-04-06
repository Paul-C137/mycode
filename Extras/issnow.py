#!/usr/bin/python3
"""Author:  Paul Lack | API review
Given the data contained within issnow, available from:

http://api.open-notify.org/iss-now.json

Write a program that displays the current:

Time, Lat, and Long
"""

issnow = {"message": "success", "timestamp": 1617722192, "iss_position":  \
         {"longitude": "138.7348", "latitude": "-42.5022"}}

time_now = issnow.get("timestamp")
station_lat = issnow.get("iss_position").get("latitude")
station_long = issnow.get("iss_position").get("longitude")

print(station_lat)

print(f"At, {time_now} the iss will be at {station_lat} degrees latitude and {station_long} degrees longitude.")