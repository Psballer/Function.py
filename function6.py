def minimum_numbers(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
numbers = [8, 4, 9, 2, 5, 7, 3]
result = minimum_numbers(numbers)
print(result)
