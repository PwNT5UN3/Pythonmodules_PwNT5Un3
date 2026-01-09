def ft_count_harvest_iterative():
    iterator = 1
    days_until = int(input('Days until harvest: '))
    while iterator in range(days_until):
        print(f'Day {iterator}')
        iterator += 1
    print(f'Day {iterator}')
    print('Harvest time!')
