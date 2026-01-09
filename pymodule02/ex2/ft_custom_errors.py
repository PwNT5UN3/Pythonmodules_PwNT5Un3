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


def check_plants(plant_health: str):
    '''A test wether a plant is dead or not'''
    if plant_health == 'dead':
        raise PlantError('The Plant is wilting')
    else:
        print('The Plant is fine')


def test_water(water_quality: str):
    '''A test wether the water is poisonous or not'''
    if water_quality == 'poisoned':
        raise WaterError('The Water is poisonous')
    else:
        print('The Water is fine')


def test_errors():
    '''A tester for the garden exceptions'''
    print('=== Custom Garden Errors Demo ===')
    print('\nTesting PlantError...')
    try:
        check_plants('dead')
    except Exception as e:
        print(e)
    try:
        check_plants('fine')
    except Exception as e:
        print(e)
    print('\nTesting WaterError...')
    try:
        test_water('poisoned')
    except Exception as e:
        print(e)
    try:
        test_water('fine')
    except Exception as e:
        print(e)
    print('\nTesting all errors...')
    try:
        check_plants('dead')
    except Exception as e:
        print(e)
    try:
        check_plants('fine')
    except Exception as e:
        print(e)
    try:
        test_water('poisoned')
    except Exception as e:
        print(e)
    try:
        test_water('fine')
    except Exception as e:
        print(e)
    print('\nAll custom errors tested!')


if __name__ == '__main__':
    test_errors()
