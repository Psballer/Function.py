def maximum_numbers(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
numbers = [8, 4, 9, 2, 5, 7, 3]
result = maximum_numbers(numbers)
print(result)
