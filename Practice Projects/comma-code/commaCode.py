def to_str(list):

    r = ''
    
    for i in list:
        if i == list[-1]:
            r += 'and ' + i
        else:
            r += i + ', '

    return r

spam = ['apples', 'bananas', 'tofu', 'cats']
print(to_str(spam))
