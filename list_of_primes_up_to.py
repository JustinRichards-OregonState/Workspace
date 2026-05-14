def list_primes_to(limit=100):

    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False 
    #makes sure that 1 and 0 aren't read as prime numbers

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i] == True:
            for j in range(i * 2, limit + 1, i):
                is_prime[j] = False

    primes = []
    for i in range(limit + 1):
        if is_prime[i] == True:
            primes.append(i)
            #append adds a single item to the end of the list, which is good for loops.

    return primes

End = list_primes_to(limit=100)
print(End)

#you can change the 100 in limit=100 to anything to change the limit.