class GardenError(Exception):
    '''A basic Exception class for custom garden errors'''
    def __init__(self, message: str):
        '''the exception constructor'''
        super().__init__(message)


class PlantError(GardenError):
    '''A garden Exception relating to plant issues'''
    def __init__(self, message: str):
        '''the exception constructor'''
        super().__init__(message)

    def __str__(self) -> str:
        '''the exception error message'''
        return f'PlantError: {self.args[0]}!'


class WaterError(GardenError):
    '''A garden Exception relating to water issue'''
    def __init__(self, message: str):
        '''the exception constructor'''
        super().__init__(message)

    def __str__(self) -> str:
        '''the exception error message'''
        return f'WaterError: {self.args[0]}!'


class WateringException(GardenError):
    '''A custom Exception related to issues with the watering system'''
    def __init__(self, plant: str) -> None:
        '''the exception constructor'''
        super().__init__(plant)

    def __str__(self) -> str:
        '''the custom exception message'''
        return f'WateringError: cannot water {self.args[0]} - invalid plant!'


class Plant:
    '''defines a plant with name, waterlevel and sunlight hours'''
    def __init__(self, name: str, water_level: int, sun_hours: int) -> None:
        '''creates a new plant'''
        self.name = name
        self.water_level = water_level
        self.sun_hours = sun_hours


class GardenManager:
    '''a management system for a garden'''
    def __init__(self, waterlevel: int) -> None:
        '''creates a new garden manager'''
        self.plants = []
        self.waterlevel = waterlevel

    def add_plant(self, plant: Plant):
        '''adds a new plant to the garden'''
        try:
            if plant.name == '':
                raise GardenError("Error adding plant: Name can't be empty!")
            else:
                self.plants.append(plant)
                print(f'Added {plant.name}')
        except Exception as e:
            print(e)

    def water_plants(self):
        '''waters all the plants'''
        try:
            for plant in self.plants:
                if not plant:
                    raise WateringException(plant)
                else:
                    print(f'Watering {plant.name}...')
                    plant.water_level += 5
        except Exception as e:
            print(e)
        finally:
            print('Closing watering system')

    def check_plant_health(self):
        '''checks the health of all plants'''
        for plant in self.plants:
            try:
                name = plant.name
                if plant.name == '':
                    raise PlantError(f'{name} has no name')
                if plant.water_level > 10:
                    raise PlantError(f'{name} is overwatered')
                if plant.water_level < 1:
                    raise PlantError(f'{name} is drying out')
                if plant.sun_hours > 12:
                    raise PlantError(f'{name} is getting too much sunlight')
                if plant.sun_hours < 2:
                    raise PlantError(f'{name} is getting not enough sunlight')
                print(f'{plant.name}: Healthy ',
                      f'(water: {plant.water_level}, sun: {plant.sun_hours})')
            except Exception as e:
                print(e)

    def check_water(self):
        '''
        checkss if the amount of available water
        is enough to sustain the plants
        '''
        try:
            if self.waterlevel < 5:
                raise WaterError('Not enough water available')
        except Exception as e:
            print(e)


def test_garden_manager():
    '''a test for the garden manager'''
    manager = GardenManager(3)
    print('=== Garden Management System ===')
    print('\nAdding plants to garden...')
    manager.add_plant(Plant('tomato', 9, 10))
    manager.add_plant(Plant('carrot', 4, 2))
    print('\nWatering plants...')
    manager.water_plants()
    print('\nChecking plant health...')
    manager.check_plant_health()
    print('\nChecking system integrity...')
    manager.check_water()
    print('Integrity has been secured')
    print('\nTest complete!')


if __name__ == '__main__':
    test_garden_manager()
