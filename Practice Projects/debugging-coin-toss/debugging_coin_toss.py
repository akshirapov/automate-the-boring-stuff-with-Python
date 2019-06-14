#! python3
# debugging_coin_toss.py - Is a simple coin toss guessing game


import random

options = {0: 'tails', 1: 'heads'}

guess = ''
if guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = options[random.randint(0, 1)]  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
