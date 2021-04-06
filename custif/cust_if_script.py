#!/usr/bin/env python3

'''
Author:  Paul Lack
Date:    4/6/21

This program demonstrates if/elif/else.
'''

def main():

    message = input('Enter your test score from 0-100: ')
    message_int = int(message)

    if message_int <= 59:
        grade = 'F'
    elif message_int >= 60 and message_int <= 69:
        grade = 'D'
    elif message_int >= 70 and message_int <= 79:
        grade = 'C'  
    elif message_int >= 80 and message_int <= 89:
        grade = 'B'  
    else:
        grade = 'A'  
    print(f'You recieved a grade of {grade}.')
    print('Program exiting')
    exit()

main()    
 