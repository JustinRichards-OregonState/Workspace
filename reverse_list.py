def reverse_list(vals):
    left = 0
    right = len(vals) - 1

    while left < right:

        temp = vals[left]

        vals[left] = vals[right]

        vals[right] = temp
        
        left = left + 1
        right = right - 1 

vals = [7, -3, 12, 9]

reverse_list(vals)

print(vals) 