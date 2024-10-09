COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWNABLE_Y = [y for y in range(-180,250,30)]
SPAWNABLE_X = [x for x in range(300,1000,50)]


from car import Car
import random

class CarManager:
    def __init__(self):
        self.car_list = []
        for i in range(20):
            car = self.random_car()            
            self.car_list.append(car)

    def update(self):
        for car in self.car_list:
            if car.xcor() <= -300:
                c,x,y = self.random_x_y_color()
                car.respawn(c,x,y)
            else:
                car.move(STARTING_MOVE_DISTANCE)


    def random_car(self):
        c,x,y = self.random_x_y_color()
        car = Car(c,x,y)
        return car
    
    def random_x_y_color(self):
        random_x = random.choice(SPAWNABLE_X)
        random_y = random.choice(SPAWNABLE_Y)
        random_color = random.choice(COLORS)
        return random_color,random_x,random_y