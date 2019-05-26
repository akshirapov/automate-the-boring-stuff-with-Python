import random

messages = ['It is certain',
            'It is deciddly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very dobtful']

print(messages[random.randint(0, len(messages)-1)])
