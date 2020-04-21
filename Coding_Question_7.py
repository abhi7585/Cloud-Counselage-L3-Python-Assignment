def update(string):
    string_not = string.find('not')
    poor = string.find('poor')

    if poor > string_not and string_not > 0 and poor > 0:
        string = string.replace(string[string_not:(poor+4)], 'good')
        return string
    else:
        return string


print(update('The lyrics is not that poor!'))
print(update('The lyrics is poor!'))
