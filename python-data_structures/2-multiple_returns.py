#!/usr/bin/python3
def multiple_returns(sentence): 
    length = len(sentence)
    first_charcater = sentence[0]
    if length > 0:
        return "Length: {:d} - First charater: {}".format(length, first_charcater)
    else: 
        None     
        
print(multiple_returns("At Holberton school, I learnt C!"))

# def multiple_returns(sentence):
#     # Check if the sentence is empty
#     if len(sentence) == 0:
#         return (0, None)
#     else:
#         return (len(sentence), sentence[0])

# # Test the function
# input_sentence = "Hello, world!"  # Change this to the sentence you want to test
# result = multiple_returns(input_sentence)
# print(f"Length: {result[0]}, First Character: {result[1]}")
