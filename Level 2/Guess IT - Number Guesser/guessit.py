# Guessing game - Write a Python program that generates a
# random number between 1 and 100. The user should then try to user_guess the number.
# The program should provide hints such as "too high" or "too low" until the correct
# number is guessed.

import random


class Guess:
    
    # initialize instance variables
    def __init__(self):
        self.random_number = random.randint(1, 100)
        self.user_guess = None
        self.count = 0

    def intro(self):
        print('''
*******Welcome to the guessing game!*******
     Pick a number between 1 and 100
     the game will give you hints on
     your answer!
     You will win once you guess the 
     right number or if you exit
     Good luck!
    (enter 'exit' to exit out)
*******************************************
              ''')
    
    def outro(self):
        print('''
Author: Prashant Maharjan     
              ''')

    def guessr(self):
        self.intro()
        # loop until user finds the correct number
        while self.user_guess != self.random_number:
            user_input = input("What's your guess?\n> ")

            # option to exit
            if user_input.lower() == "exit":
                print("You exited the game. Thanks for playing!")
                break

            try:
                self.user_guess = int(user_input)
                self.count += 1

                # hints for the user
                if self.user_guess < self.random_number:
                    print(f"\nYour Guess is too low, go higher than {self.user_guess}")
                elif self.user_guess > self.random_number:
                    print(f"\nYour Guess is too high, go lower than {self.user_guess}")
                else:
                    print(f"You got it!!!! the right number was {self.random_number}")
                    print(f"And it only took you {self.count} tries! Well done!")
            except:
                print('Please enter integer values')

        self.outro()

# run this only if the file being run is this file
if __name__ == '__main__':
    guess = Guess()
    guess.guessr()

# Project by - Prashant Maharjan