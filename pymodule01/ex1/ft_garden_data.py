#!/usr/bin/env python3
class Plant:
    '''defines a plant'''
    def __init__(self, name: str, height: int, age: int):
        '''creates a plant object with the given parameters'''
        self.name = name
        self.age = age
        self.height = height

    def get_info(self):
        '''prints the attributes of the object'''
        print(f'{self.name}: {self.height}cm, {self.age} days old')


def make_class_rose():
    '''makes a rose, this time with class'''
    rose = Plant('Rose', 25, 30)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)
    print('=== Garden Plant Registry ===')
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()


if __name__ == "__main__":
    make_class_rose()
