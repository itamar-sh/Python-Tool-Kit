from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Concrete subclass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Example usage
def animal_sound(animal: Animal):
    print(animal.make_sound())

# Creating instances of the concrete subclasses
dog = Dog()
cat = Cat()

# Using the instances
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
