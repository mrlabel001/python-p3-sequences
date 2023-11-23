#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    fibonacci_seq = [a, b]
    while len(fibonacci_seq)<length:
        a, b = b ,a + b
        fibonacci_seq.append(b)
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        print(fibonacci_seq)