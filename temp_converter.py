# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 06:43:25 2021
@author: USER
"""

def fahrenheit_celsius_converter():
    try:
        temperature_value = int(input('Input your temperature value (integers only): '))
        expected_unit = ['c', 'C', 'f', 'F']
        unit_input = input('Input the unit to be converted from, C if Celsius, or F if Fahrenheit: ')
        while unit_input not in expected_unit:
            print("\n")
            print ("The inputted unit is not appropriate, it should be 'C' or 'F'.")
            unit_input = input('Input the unit to be converted from, C if Celsius, or F if Fahrenheit: ')
        if unit_input == 'F' or unit_input == 'f':
            celsius_equivalent = round((5/9) * (temperature_value - 32), 2)
            print (str(temperature_value) + ' Fahrenheit equates to ' + str(celsius_equivalent) + ' Celsius')
        elif unit_input == 'C' or unit_input == 'c':
            fahrenheit_equivalent = round(((1.8 * temperature_value) + 32), 2)
            print (str(temperature_value) + ' Celsius equates to ' + str(fahrenheit_equivalent) + ' Fahrenheit')
        else:
            print ('Your unit input is neither C nor F, input the appropriate unit.')
    except ValueError:
        print ('The inputted value is not an integer, enter an integer.')
        fahrenheit_celsius_converter()
        
fahrenheit_celsius_converter()
