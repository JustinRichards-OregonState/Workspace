def hailstone(n):
    "returns the number of steps it takes to reach 1 in a hailstone sequence. interger = a postiive starting interger. returns the number of steps taken to reach 1."
    
    steps = 0

    while n != 1:
        if n % 2 ==0:
            n = n //2
        else:
            n = n * 3 + 1
        steps += 1

    return steps