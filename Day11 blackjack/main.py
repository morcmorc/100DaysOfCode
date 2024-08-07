import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def give_card(to_who):
    to_who.append(random.choice(cards))
    while check_lost(to_who) and 11 in to_who:
         to_who[to_who.index(11)] = 1
    return to_who
def check_lost(list):
    if sum(list) > 21:
        return True
    else:
        return False

game_on = True
player = []
dealer = []
give_card(player)
give_card(player)
give_card(dealer)
while game_on:
    p_score = sum(player)
    print(f"Your cards: {player}, current score: {p_score}")

    if check_lost(player):
            print(f"You lost, your score: {p_score}")
            exit()

    d_score = sum(dealer)
    print(f"Dealer\'s cards: {dealer}")
    if check_lost(dealer):
            print(f"You won, dealer score: {d_score}")
            exit()
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y":
        give_card(player)
    else:
        while sum(dealer) < sum(player) and sum(dealer) <21:
            give_card(dealer)
        print(sum(dealer))
        if sum(dealer) > sum(player) and sum(dealer) <= 21:
             print(f"Dealer won with score: {sum(dealer)}")
             exit()
        elif sum(player) == sum(dealer):
             print(f"Dealer won, you have the same score: {sum(player)}")
             exit()
    
