#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from os import name


name_list = []
with open("./Input/Names/invited_names.txt") as nameFile:
    for line in nameFile.readlines():
        name = line.replace("\n","")
        name_list.append(name)
# print(name_list)

#letter
letter = ""
with open("./Input/Letters/starting_letter.txt") as letterFile:
    letter = letterFile.read()

# print(letter)

for name in name_list:
    finished_letter = letter.replace("[name]",name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt","w") as file:
        file.write(finished_letter)