def fib(n):
    "returns the fibonacci number at a given position n using a loop. a positive number that shows the position in the sequence. returns the fibonacci number at position n."

    a, b = 1, 1

    for _ in range(n - 1):
        a, b = b, a + b
    
    return a