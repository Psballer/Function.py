def repeat_string(text, number):
    if type(number) == int:
        return text * number
    return text
result = repeat_string("hello", 3)
print(result)
