def check_temperature(temp_str: str):
    '''This function takes a temperature as a string,
    attempts to convert it to a decimal number
    and checks its viability for plant habitability
    '''
    try:
        temp_int = int(temp_str)
    except Exception:
        print(f"Error: '{temp_str}' is not a decimal number!")
        return
    if temp_int > 40:
        print(f'Warning: {temp_int} degrees Celsius is too hot!')
        return
    elif temp_int < 0:
        print(f'Warning: {temp_int} degrees Celsius is too cold!')
        return


def test_temperature_input():
    '''This function gives a few test cases for check_temperature()'''
    print('=== Garden Temperature Checker ===')
    inputs = ['25', 'abc', '100', '-50']
    for test in inputs:
        print(f'\nTesting temperature: {test}')
        check_temperature(test)
    print("\nAll tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature_input()
