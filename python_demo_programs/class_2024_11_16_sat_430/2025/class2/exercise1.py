import random
from dataclasses import dataclass


class StringFoo:
    def __init__(self):
        self.message = ''

    def set_string(self, message):
        self.message = message

    def print_string(self):
        print(self.message.upper())


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length

    def display_info(self):
        area = self.calculate_area()
        print(f"Width: {self.width}, Length: {self.length}, Area: {area}")


from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * pi * self.radius


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(1, 10) + random.randint(1, 10)
        self.attack_power = random.randint(1, 6)
        self.defense_power = random.randint(1, 6)

    def make_attack(self):
        return random.randint(1, 6) + self.attack_power

    def receive_damage(self, damage):
        if damage > self.defense_power:
            self.hp -= damage - self.defense_power


@dataclass
class DnD:
    force: random.randint(1, 20)


class HeroWithAttributes(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.attributes = DnD()