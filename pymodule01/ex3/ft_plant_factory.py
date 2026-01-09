#!/usr/bin/env python3
class Plant:
    '''Defines a Plant'''
    def __init__(self, name: str, height: int, age: int):
        '''creates a plant object with the given parameters'''
        self.name = name
        self.age = age
        self.height = height

    def get_info(self):
        '''prints the attributes of the object'''
        print(f'{self.name}: {self.height}cm, {self.age} days old')

    def announce(self):
        '''Announces a plant'''
        print(f'Created: {self.name} ({self.height}cm, {self.age} days)')


def plant_factory(name: str,  height: int, age: int) -> Plant:
    '''
    A factory function that makes a plant object with the given parameters,
    announces its existence and then returns it.
    '''
    plant = Plant(name, height, age)
    return plant


def test_factory():
    '''tests the factory'''
    plants_created = 0
    rose = plant_factory('Rose', 25, 30)
    rose.announce()
    plants_created += 1
    oak = plant_factory('Oak', 200, 365)
    oak.announce()
    plants_created += 1
    cactus = plant_factory('Cactus', 5, 90)
    cactus.announce()
    plants_created += 1
    sunflower = plant_factory('Sunflower', 80, 45)
    sunflower.announce()
    plants_created += 1
    fern = plant_factory('Fern', 15, 120)
    fern.announce()
    plants_created += 1
    print(f'\nTotal plants created: {plants_created}')


if __name__ == "__main__":
    test_factory()
