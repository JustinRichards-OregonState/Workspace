F = int(input("How many integers would you like to enter?\n"))
print(f"Please enter {F} intergers.")

cheeseface = []
for i in range(F):
    amount = int(input())
    cheeseface.append(amount)

if cheeseface:
    print(f"min: {min(cheeseface)}") 
    print(f"max: {max(cheeseface)}")
else:
    print("Nothing was entered")