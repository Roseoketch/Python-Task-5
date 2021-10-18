# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:25:19 2021
@author: USER
"""
import ast


def even_numbers_in_list():
    even_numbers_list = []
    try:
        list_input = ast.literal_eval(input('Add your list here: '))
        while len (list_input) == 0:
            print ('The list is empty, kindly input numbers.')
            list_input = ast.literal_eval(input('Paste your list here: '))
            
        if all(isinstance(item, int) for item in list_input):
            print ('From the list give, the following re the even numbers:')
            for item in list_input:
                if item % 2 == 0:
                    even_numbers_list.append(item)
            if len (even_numbers_list) > 0:
                print (even_numbers_list)
            else:
                print ('Sorry, from the list, there is no even number.')
        else:
            print ('There are non-integer value(s) in the list, ensure all values are integers.')
            even_numbers_in_list()
    except (ValueError, SyntaxError):
        print ('Ensure you add correct list of integers. i.e [1,2,3,4,5,6]')
        even_numbers_in_list()
        
even_numbers_in_list()
