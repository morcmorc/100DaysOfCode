def add(*args):
    sum = 0
    # print(args[1])
    for num in args:
        sum += num
    return sum

# print(add(4,6,45,123,5,3,3))

def calculate(n, **kwargs): # wird zum dict
    print(kwargs)
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)    

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", seats=4)
print(my_car.seats)
