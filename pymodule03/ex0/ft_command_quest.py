import sys


def command_quest():
    '''takes the arguments from argv and prints them out'''
    print('=== Command Quest ===')
    if len(sys.argv) == 1:
        print('No Arguments provided!')
    else:
        print(f'Arguments received: {len(sys.argv) - 1}')
    for arg in range(len(sys.argv)):
        if arg == 0:
            print(f'Program name: {sys.argv[0]}')
        else:
            print(f'Argument {arg}: {sys.argv[arg]}')
    print(f'Total Arguments: {len(sys.argv)}')


if __name__ == '__main__':
    command_quest()
