from typing import Any


class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following =  0
    def __str__(self) -> str:
        return f"name: {self.name} and id: {self.id} with {self.followers} followers and {self.following} following"
    
    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("001","marc")
user_2 = User("002", "negin")
user_1.follow(user_2)
print(user_1)
print(user_2)
