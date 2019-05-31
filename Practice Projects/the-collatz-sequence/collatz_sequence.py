import sys


def collatz(number):

    result = 0
    
    if number % 2 == 0:
        result = number // 2
    elif number % 2 == 1:
        result = 3 * number + 1

    print(result)
    return result


try:
    number = int(input('Enter number: \n'))
except ValueError:
    print('You must enter integer.')
    sys.exit()
    
value = collatz(number)
while True:
    if value == 1:
        break
    else:
        value = collatz(value)
