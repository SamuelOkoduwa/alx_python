#!/usr/bin/python3
def multiple_returns(sentence): 
    length_of_sentence = len(sentence)
    first_charcater = sentence[0] if length_of_sentence > 0 else "None"
    return length_of_sentence, first_charcater
# print(multiple_returns("At Holberton school, I learnt C!"))        



# #!/usr/bin/python3
# def multiple_returns(sentence):
#     return (len(sentence), sentence[0] if len(sentence) > 0 else None)



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
