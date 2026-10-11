def sum_of_squares(numbers):
    return sum(num ** 2 for num in numbers)

result = sum_of_squares([2, 3, 4, 5, 7])
print(result)
