print("Welcome to the tip calculator!")
price = float(input("What was the total bill? $"))
tip_amount = float(input("How much tip would you like to give? 10, 12, or 15? "))
people_amount = int(input("How many people split the bill? "))
price = (price * (1+tip_amount*0.01))/people_amount
print(f"Each person should pay: ${price:.2f}")