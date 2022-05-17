# computer has a secret number
# we are trying to guess that secret number 

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Your guess is too low. Please try again. ')
        elif guess > random_number:
            print('Your guess is too high. Please try again. ')
            
    print(f'You guessed the number {random_number} correctly! Congradulations!!! ')



guess(10)