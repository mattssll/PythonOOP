from abc import ABC, abstractmethod


class Animal(ABC):
    type: str = NotImplemented  # if not implemented will throw an error


    @property
    @abstractmethod
    def make_sound(self):
        ...

class Horse(Animal):
    age: int
    def __init__(self, age):
        self.age = age
        #self.type = type

    def make_sound(self):
        print("uha")




h1 = Horse(25)
print(h1.age)

