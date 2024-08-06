# Auction
import os
from art import logo
b_more = True
dicto = {}
print(logo)
while b_more:
    name = input("What is your name?: ").lower()
    bid = int(input("What is your bid?: "))
    more = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    dicto[name] = bid
    
    if more == "no":
        b_more = False
    os.system("cls")
highest = 0
h_bidder = ""
for key in dicto:
    value = dicto[key]
    if value > highest:
        h_bidder = key
        highest = value
print(f"Highest bidder is {h_bidder} with {highest} $")
