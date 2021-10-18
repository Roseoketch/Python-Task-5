# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:51:38 2021
@author: USER
"""

from datetime import datetime


def get_valid_date (prompt):
    while True:
        try:
            value = datetime.fromisoformat(input(prompt))
        except (ValueError, SyntaxError):
            print ("What was typed is either not a date, or the format is inappropriate.")
            continue
        break
    return value


def days_difference_calculator ():
    start_date = get_valid_date('Type the start date in ‘YYYY-MM-DD’ format: ')
    end_date = get_valid_date('Type the end date in ‘YYYY-MM-DD’ format: ')
    days_difference = abs((end_date - start_date).days)
    print ('The difference in days between the two dates is ' + str(days_difference) + ' day(s).')
    
days_difference_calculator()