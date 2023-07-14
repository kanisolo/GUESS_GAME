"""
Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
"""

import random

num = random.randint(1,100)

print(
    """
    WELCOME TO GUESS ME
    I'm thinking of a number between 1 and 100
    If your guess is more than 10 away from my number, I'll tell you you're COLD
    If your guess is within 10 of my number, I'll tell you you're WARM
    If your guess is father than your most recent guess, I'll say you're getting COLDER
    If your guess is closer than your most recent guess, I'll say you're getting WARMER
    LET's PLAY!
    """)

guesses = [0]

while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n What is your guess? "))

    #check if player guess is within bounds
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    #check if the guess is correct
    if guess == num:
        print(f'CONGRATULATIONS, YOU Guessed IT IN ONLY {len(guesses)} GUESSES!!')
        break
    
    #when the guess is wrong append it
    guesses.append(guess)

    #Check if the  last guess was closer or further from the num
    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER')
        else:
            print('COLDER')
    else:
        if abs(num - guess) <= 10:
            print('WARM')
        else:
            print('COLD')


    
    