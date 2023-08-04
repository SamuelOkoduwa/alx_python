#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if sentence == ():
        first == None
    else:
        return (length, first)
 

# def multiple_returns(sentence):
#     return (len(sentence), sentence[0] if len(sentence) > 0 else None)
# print(multiple_returns("At Holberton school, I learnt C!"))