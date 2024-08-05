

alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def main():
    while True:
        type = input("Type 'encode' to encrypt, type 'decode' to decrypt \n").lower()
        text = input("Type your message: \n").lower()
        number = int(input("Type the shift number:\n"))
        if type == "encode":
            encode(text=text,number=number)
        elif type == "decode":
            decode(text=text,number=number)
        else:
            print("I can only encode or decode")
            exit()
        again = input("Do you want to go again? (yes,no)\n").lower()
        if again != "yes":
            print("Goodbye")
            exit()

# print(len(alphabeth)) = 26
def encode(text, number):
    encoded_text = ""
    for letter in text:
        pos_alpha = alphabeth.index(letter)
        new_pos = (pos_alpha + number)%26
        encoded_text += alphabeth[new_pos]
    print(encoded_text)

def decode(text, number):
    decoded_text = ""
    for letter in text:
        pos_alpha = alphabeth.index(letter)
        new_pos = (pos_alpha - number)%26
        decoded_text += alphabeth[new_pos]
    print(decoded_text)   

# encode("baumhaus",20)
# decode("vuogbuom",20)
main()