#!/usr/bin/env python3
def convert_to_celsius(fahrenheit): 
    return float((5/9)*(fahrenheit - 32))
print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(32))