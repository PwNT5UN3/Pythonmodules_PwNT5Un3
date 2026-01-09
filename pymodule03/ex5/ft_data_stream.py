def event_generator(event_num: int):
    '''This generator creates somewhat randomised events'''
    players_list = ['alice', 'bob', 'charlie', 'david', 'emma']
    events_list = ['killed monster', 'found treasure', 'leveled up']

    for i in range(event_num):
        player = players_list[i % len(players_list)]
        level = (i % 20) + 1
        event = events_list[i % len(events_list)]

        output = {'player': player, 'level': level, 'event': event}
        yield output


def generator_test():
    '''tests the event generator and prints the first 10 events formatted'''
    print('=== Event generator demo ===')
    print('\nProcessing 1000 events...\n')
    event_gen = event_generator(1000)
    for i in range(10):
        current = next(event_gen)
        player = current['player']
        level = current['level']
        event = current['event']
        print(f'Event {i + 1}: {player} (Level{level}) {event}')


def fibonacci_generator():
    '''generates the first 10 numbers of the fibonacci sequence'''
    x = 0
    y = 1
    yield x
    yield y
    for num in range(8):
        yield x + y
        if num % 2 == 0:
            x = x + y
        else:
            y = x + y


def fibb_test():
    '''tests the  fibonacci generator'''
    print('Fibonacci Numbers (first 10): ', end='')
    nums = fibonacci_generator()
    for num in range(9):
        print(next(nums), end=', ')
    print(next(nums))


def is_prime(num):
    '''checks if a number is prime'''
    test = 2
    while test < (num / 2) + 1:
        if num % test == 0:
            return False
        test += 1
    return True


def prime_generator():
    '''generates the first 5 prime numbers'''
    num = 2
    for _ in range(5):
        while True:
            if is_prime(num):
                yield num
                num += 1
                continue
            num += 1


def prime_test():
    '''tests the prime generator'''
    print('Prime Numbers (first 5): ', end='')
    nums = prime_generator()
    for _ in range(4):
        print(next(nums), end=', ')
    print(next(nums))


if __name__ == '__main__':
    generator_test()
    print('\n=== Generator  demonstration ===')
    fibb_test()
    prime_test()
