F = int(input("Enter the integer for the player to guess.\n"))

guess = None
Tries = 0

while guess != F:
    if Tries == 0:
        guess = int(input("Enter your guess.\n"))
    else:
        if guess > F:
            Taxes = "Too high -try again:\n"
        else:
            Taxes = ("Too low - try again\n")
        guess = int(input(Taxes))

    Tries += 1

print(f"You guessed it in {Tries} tries.")