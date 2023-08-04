def best_score(a_dictionary):
    highest_score = max(a_dictionary)
    if highest_score == max(a_dictionary):
        return highest_score
    elif not a_dictionary:
        return None
print(best_score({'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}))
