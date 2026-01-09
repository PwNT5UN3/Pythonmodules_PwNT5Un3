print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n')
try:
    print('Establishing connection...')
    vault = open('ancient_fragment.txt', 'r')
    print(f'Connection establshed: {vault.name}\n')
    print('Recovering data...\n')
    for line in vault:
        print(f'Fragment recovered: {line}')
    print('\nAll fragments recovered. Disconnecting data vault...')
    vault.close()
except FileNotFoundError:
    print('ERROR: Storage vault not found. Run data generator first.')
