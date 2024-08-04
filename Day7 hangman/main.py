# hangman
import random
import hangman_words
from hangman_art import logo,stages


from numpy import disp

word_list = hangman_words.word_list
choosen_word = random.choice(word_list)

display =["_"]*len(choosen_word)


lifes = 6

print(stages[lifes])
print(display) 

while lifes > 0:
    guess = input("Guess a letter: ").lower()

    if guess not in choosen_word:
        lifes -= 1
        if lifes == 0:
            print(stages[lifes])
            print(f"You lost! The word was: {choosen_word}")
            break
        else:
            print(f"Wrong, you have {lifes} left.")
    else:
        for position in range(len(choosen_word)):
            if choosen_word[position] == guess:
                display[position] = guess
        
    print(stages[lifes])
    print(display)
    if "_" not in display:
        print("YOU WON!")
        break
