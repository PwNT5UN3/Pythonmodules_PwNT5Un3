#!/usr/bin/env python3
class Plant:
    '''Defines a plant'''
    def __init__(self, name: str, height: int, age: int):
        '''initialies a base plant'''
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    '''Defines a Flower as a Plant subclass'''
    def __init__(self, name: str, height: int, age: int, color: str):
        '''crates a Flower object'''
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        '''lets the flower bloom'''
        print(f'{self.name} is blooming in a nice {self.color} shade!')


class Oak(Plant):
    '''Defines an Oak as a Plant subclas'''
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        '''creates an Oak object'''
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        '''lets the oak make a shadow'''
        shade = (self.height / 100) * (self.trunk_diameter / 100)
        print(f'{self.name} provides {shade} m^2 of shade')


class Vegetable(Plant):
    '''Defines a vegetable as a Plant Subclass'''
    def __init__(
                self, name: str,
                height: int,
                age: int,
                harvest_season: str,
                nutricional_value: int
                ):
        '''makes a vegetable object'''
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrional_value = nutricional_value


def ft_plant_types():
    '''Tests the inherited plant subclasses'''
    rose = Flower('Rose', 30, 10, 'red')
    rose.bloom()
    lavender = Flower('Lavender', 50, 5, 'purple')
    lavender.bloom()
    old_oak = Oak('Old oak', 10000, 36500, 50)
    old_oak.produce_shade()
    young_oak = Oak('Young oak', 2000, 300, 5)
    young_oak.produce_shade()
    potato = Vegetable('Potato', 8, 30, 'Fall season', 140)
    print(potato.name)
    carrot = Vegetable('Carrot', 20, 50, 'Spring season', 200)
    print(carrot.name)


if __name__ == '__main__':
    ft_plant_types()
