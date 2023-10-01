#!/usr/bin/env python3

'''def fibonacci_sequence(n):
    fib_sequence = []
    a = 0
    b = 1
    for _ in (n):
        fibonacci_sequence.append(a)
        a = b
        b = a + b
        return fib_sequence
    
print(fibonacci_sequence(8))'''

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    return fib_sequence

# Example usage:
# n = 10
# result = fibonacci_sequence(n)
# print(result)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

