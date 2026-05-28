def count_letters(text):
    letter_counts = {}
    
    upper_text = text.upper()
    
    for char in upper_text:
        if char.isalpha() and char not in letter_counts:
            letter_counts[char] = upper_text.count(char)
            
    return letter_counts

print(count_letters("Abbabxa"))