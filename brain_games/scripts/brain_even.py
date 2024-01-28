#!/usr/bin/env python3

import random


def main_even():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name?', end='')
        name = input()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_1 = random.randint(1,100)
    print('Question:',number_1)
    answer = ''
    print('Your answer:', end='')
    answer = input()
    if number_1 % 2 == 0 and answer == 'yes':
        print('Correct!')
    if number_1 % 2 != 0 and answer == 'no':
        print('Correct!')
    if number_1 % 2 == 0 and answer != 'yes':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'")
        print(f"Let's try again, {name}!")
    if number_1 % 2 != 0 and answer != 'no':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'")
        print(f"Let's try again, {name}!")

if __name__ == '__main_even__':
    main_even()
