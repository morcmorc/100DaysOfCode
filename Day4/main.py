# rock paper sisccors
import random

# import my_module
# print(my_module)

# random_integer = random.randint(0,2)
# print(random_integer)

#List append 1
#List extend adds List

#RPS
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Hello to Rock Paper Scissors World Championship\n")
player = input('Write: \n"0" or "Rock", \n"1" or "Paper" or \n"2" or "Scissors" \nto choose a move.\n')
match player:
    case "Rock":
        player = 0
    case "Paper":
        player = 1
    case "Scissors":
        player = 2
    case _:
        player = int(player)


#print player as asci
asc_list = [rock, paper, scissors]
print(f"You chose:\n "+asc_list[player])

#Bot Logic
bot = random.randint(0,2)
print("Bot chose:\n " +asc_list[bot])

if((player == 0 and bot == 2)
   or (player == 1 and bot == 0)
   or (player == 2 and bot == 1) ):
    print("You Won, lucky person!")
elif(player == bot):
    print("Draw, thats lame...")
else:
    print("You lost, loser!")