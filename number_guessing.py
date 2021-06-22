#!/usr/bin/env python3

from random import randint


def number_guessing():
    
    number_guessed = randint(1,10)
    number_of_guesses = 3

    for guess in range(1, number_of_guesses+1):
        number = int(input('[+] Enter number: '))
        
        if number != number_guessed:
            if number < number_guessed:
                print('{} is too low'.format(number))
                continue
            else:
                print('{} is too high'.format(number))
                continue
        else:
            if guess == 1:
                print('Excellent you got it on the first try')
                break
            elif guess == 2:
                print('Very good you got it on the second try')
                break
            else:
                print('Good you got it on the last try')
                break
    else:
        print("Sorry, you didn't get the right answer")


if __name__ == '__main__':
    number_guessing()

