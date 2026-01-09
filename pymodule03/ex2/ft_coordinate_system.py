import sys
import math


def calc_dist_from_0_0_0(coordinates: tuple[int, int, int]):
    '''
    takes a tuple of ints representing 3d space coordinates
    and gives the lenght of a vector
    describing the move from 0, 0, 0 to that coordinates
    '''
    x = coordinates[0] ** 2
    y = coordinates[1] ** 2
    z = coordinates[2] ** 2
    return math.sqrt(x + y + z)


def coordinate_system():
    '''
    takes three arguments from argv,
    converts them to a tuple of ints representing coordinates,
    prints them
    and the distance from 0, 0, 0 to them
    '''
    print('=== Game Coordinate System ===')
    if len(sys.argv) != 4:
        print('Invalid coordinates entered! Expected <x> <y> <z>!')
        return
    try:
        coordinates = (
                        int(sys.argv[1]),
                        int(sys.argv[2]),
                        int(sys.argv[3])
                      )
    except Exception:
        print('Invalid coordinates! Please enter decimal numbers only!')
        return
    print(f'Parsed position: {coordinates}')
    print(f'Distance from (0, 0, 0) to {coordinates}: ',
          f'{calc_dist_from_0_0_0(coordinates)}')
    print('\nUnpacking position:')
    print('Player at ',
          f'x={coordinates[0]}, y={coordinates[1]}, z={coordinates[2]}')


if __name__ == '__main__':
    coordinate_system()
