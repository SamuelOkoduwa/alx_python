#!/usr/bin/python3

def is_same_class(obj, a_class):
    return type(obj) is a_class

# Sample class
class Myclass:
    pass

my_instance = Myclass()

# Returning true because the obbject is exactly an instance of the specified class
result = is_same_class(my_instance, Myclass)
print(result)

# Returning false because the obbject is not exactly an instance of the specified class
result = is_same_class(42, int)
print(result)