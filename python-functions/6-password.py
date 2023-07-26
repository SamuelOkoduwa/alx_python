#!/usr/bin/env python3

def validate_password(password):
    valid = True
    if len(password) < 8:
        print('length should be at least 8')
        valid = False       
    if not any(char.isdigit() for char in password):
        print("Password should have at least a digit")
        valid = False
    if not any(char.isupper() for char in password):
        print("Password should have at least an uppercase")
        valid = False
    if not any(char.islower() for char in password):
        print("Password should have at least a lowercase")
        valid = False
    if any(char.isspace() for char in password):
        valid = False
    return valid

# def validate_password(password):
#     is_valid = True 
#     if len(password) < 8: 
#         is_valid = False    
#     if not any(char.isdigit() for char in password): 
#         is_valid = False
          
#     if not any(char.isupper() for char in password): 
#         is_valid = False     
#     if not any(char.islower() for char in password):  
#         is_valid = False
#     if any(char.isspace() for char in password): 
#         is_valid = False
#     return is_valid 
print(validate_password(input(" Please type your Password:")))