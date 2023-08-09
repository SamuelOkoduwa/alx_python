#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = list(map((lambda n: n * number), my_list))
    return new_list

# print (multiply_list_map([2,4,5,6,7], 4))

