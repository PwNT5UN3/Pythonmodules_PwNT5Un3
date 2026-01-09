def garden_operations(error: str):
    '''
    This function takes an errortype as string
    and demonstrates how the error might appear
    '''
    if error == 'ValueError':
        try:
            print("Attempting to convert 'abc' to decimal number...")
            int('abc')
        except ValueError:
            print('Caught ValueError')
    elif error == 'ZeroDivisionError':
        try:
            print('Attempting to divide by 0...')
            x = 0/0
            print(x)
        except ZeroDivisionError:
            print('Caught ZeroDivisionError')
    elif error == 'FileNotFoundError':
        try:
            print('Attempting to open a nonexistent file...')
            open('missing.txt', 'r')
        except FileNotFoundError:
            print('Caught FileNotFoundError')
    elif error == 'KeyError':
        try:
            print('Attempting to grab info from a nonexistent key...')
            test_dict = {}
            test_dict['test']
        except KeyError:
            print('Caught KeyError')
    else:
        try:
            print('Attempting all previous tests at once...')
            error_int = int(error)
            error_int = 0/error_int
            open('error', 'r')
            test_dict = {}
            test_dict[error]
        except Exception:
            print("Caught an error but didn't crash...")


def test_error_types():
    '''This function tests garden_operations()'''
    print('=== Garden Error Types Demo ===')
    errors = [
                'ValueError',
                'ZeroDivisionError',
                'FileNotFoundError',
                'KeyError'
            ]
    for error in errors:
        print(f'\nTesting {error}...')
        garden_operations(error)
    print('')
    garden_operations('0')
    print('\nAll error types tested successfully!')


if __name__ == '__main__':
    test_error_types()
