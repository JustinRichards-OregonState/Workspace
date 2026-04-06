cents = int(input("Please enter an amount in cents less than a dollar."))

quarters = cents // 25
cents %= 25

#// seems to round

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

print("Your change will be:")
print("Q: ", quarters)
print("D: ", dimes)
print("N: ", nickels)
print("P: ", pennies)

