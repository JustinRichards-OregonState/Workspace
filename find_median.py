def find_median(numbers):

    sorted_numbs = sorted(numbers)
    n = len(sorted_numbs)

    if n == 0:
        return None

    mid = n // 2

    if n % 2 != 0:
        return sorted_numbs[mid]
    else:
        return(sorted_numbs[mid - 1] + sorted_numbs[mid]) / 2

some_nums = [13,7,-3,82,4]
result = find_median(some_nums)
print(result)