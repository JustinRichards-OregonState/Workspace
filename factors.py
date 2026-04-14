F = int(input("Please enter a postive integer: "))
print(f"The factors of {F} are:\n")

for i in range(1, F + 1):

    if F % i == 0:
        print(i)
