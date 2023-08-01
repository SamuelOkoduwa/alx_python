#!/usr/bin/env python3

# def is_prime(number):
#     if number % 2 == 1 and number % number == 0:
#         return True
#     else:
#         return False
        
# print(is_prime(15))

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if (number%i) == 0:
            return False
    return True