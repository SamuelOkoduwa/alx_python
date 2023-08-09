#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest_score = max(a_dictionary, key=a_dictionary.get)
    return highest_score
    
# print(best_score({'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}))
# print(best_score({}))

# def best_score(a_dictionary):
#     if not a_dictionary:
#         return None
#     bestScore = 0
#     bestScore_key = ""
#     for key, value in a_dictionary.items():
#         if value > bestScore:
#             bestScore = value
#             bestScore_key = key
#     return bestScore_key


# def best_score(a_dictionary):
#     if not a_dictionary:
#         return (None)

#     return (max(a_dictionary, key=a_dictionary.get))
# print(best_score({'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}))
# print(best_score({}))

