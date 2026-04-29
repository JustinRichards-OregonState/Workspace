def add_surname(first_names):
    return [name + " Kardashian" for name in first_names if name.startswith("K")]

names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
print(add_surname(names))