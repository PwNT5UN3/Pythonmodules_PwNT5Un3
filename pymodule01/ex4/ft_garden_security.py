class SecurePlant:
    '''Defines a Plant with private arguments'''
    def __init__(self, name: str, age: int, height: int):
        '''Creates a plant object with the given values,
        setting the numerical arguments to zero if invalid values are entered,
        accompanied with a warning message'''
        self._name = name
        if age >= 0:
            self._age = age
        else:
            self._age = 0
            print('Invalid Age entered, defaulting to 0.')
        if height >= 0:
            self._height = height
        else:
            self._height = 0
            print('Invalid Height entered, defaulting to 0.')

    def get_name(self):
        '''returns the plant name'''
        return self._name

    def get_height(self):
        '''returns the plant height'''
        return self._height

    def get_age(self):
        '''returns the plant age'''
        return self._age

    def set_name(self, new: str):
        '''sets the plant name'''
        self._name = new

    def set_age(self, new: int):
        '''sets the plant age if a valid value is given'''
        if new < 0:
            print('Invalid Age entered, age not changed.')
            return
        self._age = new

    def set_height(self, new: int):
        '''sets the plant height if a valid value is given'''
        if new < 0:
            print('Invalid Height entered, height not changed.')
            return
        self._height = new


def try_secure_plant():
    '''tests the secure plant class'''
    valid = SecurePlant('Rose', 10, 40)
    invalid = SecurePlant('Oak', -2, -6)
    valid.set_height(-5)
    invalid.get_age()


if __name__ == '__main__':
    try_secure_plant()
