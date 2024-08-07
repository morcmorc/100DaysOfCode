from art import logo,vs
from game_data import data
import random
import os


def format_data (account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}."

def select_random():
    return random.choice(data)

def check_follower(account):
    return account["follower_count"]

# print(logo)
# highscore
highscore = 0
game_on = True
os.system("cls")
winner = select_random()
while game_on:
    print(logo)
    if highscore != 0:
        print(f"You\'re right! Current score: {highscore}")
    # Person A
    # print(select_random())
    account_A = winner
    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    # Person B
    account_B = select_random()
    print(f"Against B: {format_data(account_B)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    follower_a = check_follower(account_A)
    follower_b = check_follower(account_B)
    if (guess == "a" and follower_a > follower_b) or (guess == "b" and follower_b > follower_a) :
        highscore += 1
        if follower_a > follower_b:
            winner = account_A
        else:
            winner = account_B
        os.system("cls")
    else:
        os.system("cls")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {highscore}")
        exit()


#check if right answer
#if not show highscore and end
