#!/usr/bin/env python3

def fibonacci_sequence(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        Fst = fibonacci_sequence(n - 1)
        Fst.append(Fst[-1] + Fst[-2])
        return Fst
# print(fibonacci_sequence(8))

