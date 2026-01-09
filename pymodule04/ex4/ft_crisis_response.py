print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===')
print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
try:
    with open('lost_archive.txt', 'r') as archive:
        print(f'SUCCESS: Archive recovered: {archive.read()}')
        print('STATUS: Normal operations resumed\n')
except FileNotFoundError:
    print('RESPONSE: Archive not found in storage matrix')
    print('STATUS: Crisis handled, system stable\n')
except PermissionError:
    print('RESPONSE: Archive access denied')
    print('STATUS: Crisis handled, system stable\n')
except Exception:
    print('RESPONSE: Unexpected Error occured')
    print('STATUS: Crisis handled, system stable')
print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
try:
    with open('classified_vault.txt', 'r') as archive:
        print(f'SUCCESS: Archive recovered: {archive.read()}')
        print('STATUS: Normal operations resumed\n')
except FileNotFoundError:
    print('RESPONSE: Archive not found in storage matrix')
    print('STATUS: Crisis handled, system stable\n')
except PermissionError:
    print('RESPONSE: Archive access denied')
    print('STATUS: Crisis handled, system stable\n')
except Exception:
    print('RESPONSE: Unexpected Error occured')
    print('STATUS: Crisis handled, system stable')
print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
try:
    with open('standard_archive.txt', 'r') as archive:
        print(f'SUCCESS: Archive recovered: {archive.read()}')
        print('STATUS: Normal operations resumed\n')
except FileNotFoundError:
    print('RESPONSE: Archive not found in storage matrix')
    print('STATUS: Crisis handled, system stable\n')
except PermissionError:
    print('RESPONSE: Archive access denied')
    print('STATUS: Crisis handled, system stable\n')
except Exception:
    print('RESPONSE: Unexpected Error occured')
    print('STATUS: Crisis handled, system stable')
