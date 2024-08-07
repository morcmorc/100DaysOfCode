# Guess the number
import random

def main():
    print("Welcome to the Number Geussing Game!")
    print("I\'m thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "hard":
        attempts = 5
    else:
        attempts = 10
    my_number = random.randint(0,100)
    print(f"number = {my_number}")

    while attempts > 0: 
        print(f"You have {attempts} remaining to guess the number")

        

        # make guess
        guess = int(input("Make a guess: "))
        if guess < my_number:
            print("Too low.")
        elif guess > my_number:
            print("Too high")
        elif guess == my_number:
            print(f"You got it! the number was {guess}.")
            exit()

        # if hard, lose life
        attempts -= 1
        
    print("You lost, 0 attempts remaining")





main()