a = 7
b = 4
def multiply(a, b):
    if b == 1:
        return a
    return a + multiply(a, b - 1)

print(multiply(a, b))