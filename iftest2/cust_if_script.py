#!/usr/bin/env python3

'''
Author:  Paul Lack
Date:    4/6/21

This program demonstrates if/elif/else.
'''

message = 'Enter your test score from 0-100: '

if message <= 59:
    grade = 'F'
elif message >= 60 and message <= 69:
    grade = 'D'
elif message >= 70 and message <= 79:
    grade = 'C'  
elif message >= 80 and message <= 89:
    grade = 'B'  
else:
    grade - 'A'  
print(f'You recieved a grade of {message}.')
print('Program exiting')
exit()
 