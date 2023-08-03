#!/usr/bin/env/python3

def no_c(my_string):
    remove_c_C = ""
    for char in my_string:
        if char != "c" and char != "C":
            remove_c_C += char
    return remove_c_C

# print(no_c("Character"))
# print(no_c("There are Charitable carts in Cameron"))