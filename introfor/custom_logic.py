#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]



print(f"Here on the {farms[0].get('name')} we like to grow:  ")
for i in farms[0].get('agriculture'):
	print(i)


print(f"Here on the {farms[1].get('name')} we like to grow:  ")
for i in farms[1].get('agriculture'):
	print(i)

print(f"Here on the {farms[2].get('name')} we like to grow:  ")
for i in farms[2].get('agriculture'):
	print(i)		

