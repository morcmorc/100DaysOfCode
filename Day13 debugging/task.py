
def mine():
    age = ""    
    while age is not int:
        try:
            age = int(input("How old are you: "))
            break
        except ValueError:
            print("Pls give a number")

    if age > 18:
        print(f"You can dive at age {age}.")


def stackoverflow():
    a = ''
    while a.isdigit() == False:
        a = input('Enter a number: ')

    print('You entered {}'.format(a))

mine()
stackoverflow()