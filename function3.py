def add_letters(string):
    if len(string) < 3:
        return string
    elif string.endswith('ing'):
        return string + 'ly'
    else:
        return string + 'ing'


print(add_letters('abc'))
print(add_letters('string'))
print(add_letters('on'))      
