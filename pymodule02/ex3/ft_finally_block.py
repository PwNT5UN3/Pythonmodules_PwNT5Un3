class WaterException(Exception):
    '''A custom Exception related to issues with the watering system'''
    def __init__(self, plant: str) -> None:
        '''the exception constructor'''
        super().__init__(plant)

    def __str__(self) -> str:
        '''the custom exception message'''
        return f'WateringError: cannot water {self.args[0]} - invalid plant!'


def water(plant: str):
    '''The function watering the individual plants'''
    valid_plants = ['carrot', 'tomato', 'potato', 'rice']
    if plant not in valid_plants:
        raise WaterException(plant)
    else:
        print(f'Watering {plant}')


def water_plants(plant_list: list):
    '''thw overarching atering protocol'''
    print('Starting watering protocol...')
    try:
        for plant in plant_list:
            water(plant)
    except Exception as e:
        print(e)
    finally:
        print('Stoppping watering protocol...')


def test_watering_system():
    '''a test for the watering system'''
    good_list = ['carrot', 'potato', 'rice']
    bad_list = ['rice', 'apple', 'carrot']
    print('=== Garden Watering System Demo ===')
    print('\nTesting normal operations...')
    water_plants(good_list)
    print('')
    print('Testing problematic operations...')
    water_plants(bad_list)
    print('\n=== End of Demo ===')


if __name__ == '__main__':
    test_watering_system()
