#!/usr/bin/python3
def multiple_returns(sentence): 
    if len(sentence) == 0:
        return "None"
    else:
        return(f"Length: {len(sentence)} - First character: {sentence[0]}")
        # return(len(sentence), "- First character", sentence[0])
# print(multiple_returns("At Holberton school, I learnt C!"))