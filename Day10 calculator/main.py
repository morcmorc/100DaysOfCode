
def add (n1, n2):
    return n1 + n2
def sub (n1, n2):
    return n1 - n2
def mul (n1, n2):
    return n1 * n2
def div (n1, n2):
    return n1 / n2


f_number = float(input("What\'s the first number?: "))
while True:
    print("Operation: + - * /")
    operation = input("Pick an operation: ")
    number = float(input("What\'s the next number?: "))
    match operation:
        case "+":
            res = add(f_number,number)
        case "-":
            res = sub(f_number,number)
        case "*":
            res = mul(f_number,number)
        case "/":
            res = div(f_number,number)
        case default:
            print("Error, wrong operator")
    print(f"{f_number} {operation} {number} = {res}")
    again = input(f"Type 'y' to continue with {res} or 'n' to start a new calculation or stop with 's': ")
    if again == "y":
        f_number = res
    elif again == "n":
        f_number = float(input("What\'s the first number?: "))
    else:
        exit()
    




        