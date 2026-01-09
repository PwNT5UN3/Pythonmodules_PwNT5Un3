print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===')
print('\nInitiating secure vault access...')
with open('classified_data.txt', 'r') as vault:
    print('Vault connection established with failsafe protocols\n')
    print('SECURE EXTRACTION:')
    print(vault.read())
    print()
with open('classified_data.txt', 'a') as vault:
    with open('security_protocols.txt', 'r') as protocols:
        print('SECURE PRESERVATION:')
        protocol = protocols.read()
        print(protocol)
        vault.write('\n')
        vault.write(protocol)
