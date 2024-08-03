import random
import string

from numpy import number

print("Welcome to the PyPassword Generator!")
nbr_letters = int(input("How many letters would you like in your password?"))
nbr_symbols = int(input("How many symbols would you like?"))
nbr_numbers = int(input("How many numbers would you like?"))

password = []

# letters
letters = list(string.ascii_lowercase)
for i in range(nbr_letters):
    # rnd_letter = random.randint(0,len(letters)-1)
    # password.append(letters[rnd_letter])
    password.append(random.choice(letters))

# sybols
symbols = ["@", "§","$","%","{","!","?"]
for i in range(nbr_symbols):
    # rnd_nbr = random.randint(0,len(symbols)-1)
    # password.append(symbols[rnd_nbr])
    password.append(random.choice(symbols))

# numbers 
numbers = ["0","1","2","3","4","5","6","7","8","9"]
for i in range(nbr_numbers):
    # rnd_nbr = random.randint(0,len(numbers)-1)
    # password.append(numbers[rnd_nbr])
    password.append(random.choice(numbers))

print(password)
random.shuffle(password)
print(password)
pw = ""
for c in password:
    pw += c
print(f"your password is: {pw}")
