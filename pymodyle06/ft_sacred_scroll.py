import alchemy


def sacred_scroll_mastery() -> None:
    print('\n=== Sacred Scroll Mastery ===\n')
    print('Testing direct module access:')
    print(f'alchemy.elements.create_fire(): {alchemy.elements.create_fire()}')
    print('alchemy.elements.create_water(): ' +
          f'{alchemy.elements.create_water()}')
    print('alchemy.elements.create_earth(): ' +
          f'{alchemy.elements.create_earth()}')
    print(f'alchemy.elements.create_air(): {alchemy.elements.create_air()}')
    print('\nTesting pakage-level access (controlled by __init__.py):')
    print(f'alchemy.elements.create_fire(): {alchemy.create_fire()}')
    print(f'alchemy.elements.create_water(): {alchemy.create_water()}')
    try:
        print(f'alchemy.elements.create_earth(): {alchemy.create_earth()}')
    except AttributeError:
        print('alchemy.elements.create_earth(): AttributeError - not exposed')
    try:
        print(f'alchemy.elements.create_air(): {alchemy.create_air()}')
    except AttributeError:
        print('alchemy.elements.create_air(): AttributeError - not exposed')
    print('\nPackage metadata:')
    print(f'Version: {alchemy.__version__}')
    print(f'Author: {alchemy.__author__}')


if __name__ == '__main__':
    sacred_scroll_mastery()
