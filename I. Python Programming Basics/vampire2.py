name = input('Name: ')
age = int(input('Age: '))

if name == 'Alice':
    print('Hello Alice')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not a undead, immortal vampire.')
