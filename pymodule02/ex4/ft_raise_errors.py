def check_plant_health(
                        plant_name: str,
                        water_level: int,
                        sunlight_hours: int
                       ):
    '''
    This function tests if a plant should be healthy based on several factors
    '''
    if plant_name == '':
        raise ValueError('Plant has no name!')
    if water_level > 10:
        raise ValueError('Plant is overwatered!')
    if water_level < 1:
        raise ValueError('Plant is drying out!')
    if sunlight_hours > 12:
        raise ValueError('Plant is getting too much sunlight!')
    if sunlight_hours < 2:
        raise ValueError('Plant is getting not enough sunlight!')


def test_plant_checks():
    '''This function demonstrates the health checker'''
    print('=== Garden Plant Health Checker ===')
    print('\nTesting good values...')
    try:
        check_plant_health('tomato', 5, 10)
        print("Plant 'tomato' is healthy!")
    except Exception as e:
        print(e)
    print('\nTesting empty name...')
    try:
        check_plant_health('', 5, 10)
        print("Plant '' is healthy!")
    except Exception as e:
        print(e)
    print('\nTesting too much water...')
    try:
        check_plant_health('tomato', 15, 10)
        print("Plant 'tomato' is healthy!")
    except Exception as e:
        print(e)
    print('\nTesting not enough water...')
    try:
        check_plant_health('tomato', 0, 10)
        print("Plant 'tomato' is healthy!")
    except Exception as e:
        print(e)
    print('\nTesting too much sun...')
    try:
        check_plant_health('tomato', 5, 15)
        print("Plant 'tomato' is healthy!")
    except Exception as e:
        print(e)
    print('\nTesting not enough sun...')
    try:
        check_plant_health('tomato', 5, 1)
        print("Plant 'tomato' is healthy!")
    except Exception as e:
        print(e)
    print('\nTests concluded!')


if __name__ == '__main__':
    test_plant_checks()
