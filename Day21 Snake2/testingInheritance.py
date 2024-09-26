class Animal:
    num_eyes = 0
    def __init__(self) -> None:
        self.num_eyes = 2
    def breath(self):
        print("inhale, exhale.")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        pass
    def swim(self):
        print("swimming")
    def breath(self):
        super().breath()
        print("doing this underwater")

nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)