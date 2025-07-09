def find_range(numbers):
    if len(numbers) < 3:
        return "Range determination not possible"
    minimum = min(numbers)
    maximum = max(numbers)
    range_value = maximum - minimum
    return "Range: " + str(range_value)

numbers = [5, 3, 8, 1, 0, 4]
print(find_range(numbers))
