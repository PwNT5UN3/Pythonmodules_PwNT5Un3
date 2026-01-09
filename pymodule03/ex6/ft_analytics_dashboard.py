def list_comprehension_demo():
    '''demonstrates list comprehension'''
    print('=== List comprehension Example ===')
    scores = [200, 110, 420]
    print(f'Original scores: {scores}')
    print('Doubling all scores')
    scores = [score * 2 for score in scores]
    print(f'Doubled scores: {scores}')


def dict_comprehension_demo():
    '''demonstrates dictionary comprehension'''
    print('=== Dict comprehension Example ===')
    item_prices = {'sword': 115, 'shield': 50, 'spell_book': 350}
    print(f'Full item catalog: {item_prices}')
    cheap_items = {k: v for k, v in item_prices.items() if v < 200}
    print(f'Cheap items: {cheap_items}')


def set_comprehension_demo():
    '''demonstrates set comprehension'''
    print('=== Set comprehension Example ===')
    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(f'All numbers from 1 to 9: {nums}')
    evens = {num for num in nums if num % 2 == 0}
    print(f'Even numbers between 1 and 9: {evens}')


if __name__ == '__main__':
    print('=== Datatype comprehension ===\n')
    list_comprehension_demo()
    print()
    dict_comprehension_demo()
    print()
    set_comprehension_demo()
