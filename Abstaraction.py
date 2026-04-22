#Abstraction Class
#It is used to force child classes to implement important methods
#Abstract Class object can't be created

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")
    def eat(self):
        print("Eating Bread")

d=Dog()
d.sound()
c=Cat()
c.sound()
c.eat()
        
