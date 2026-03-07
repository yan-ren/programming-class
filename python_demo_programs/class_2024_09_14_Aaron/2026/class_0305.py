# write a Temperature class that takes celsius values and write a instance function that can convert celsius to fahrenheit
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        self.fahrenheit = None

    def to_fahrenheit(self):
        self.fahrenheit = (self.celsius * 9 / 5) + 32
        return self.fahrenheit

    def show_temperature(self):
        print(f'Current temperature in celsius {self.celsius}, in fahrenheit {self.fahrenheit}')


temp = Temperature(100)
print(temp.to_fahrenheit())
temp.celsius = temp.celsius + 20
print(temp.to_fahrenheit())

class Car:
    def __init__(self, year, color):
        self.year = year
        self.color = color

# class Toyota is using Car class as base class
class Toyota(Car):
    def __init__(self, hybrid, year, color):
        super().__init__(year, color)
        self.hybrid = hybrid

t = Toyota(True, 2020, 'black')

# Inheritance
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f'{self.name} says {self.sound}'

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'Meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'Woof')
