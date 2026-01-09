import sys

print('=== CYBER ARCHIVES - COMMS SYSTEM ===')
id = input('\nInput Stream active. Enter Archivist ID: ')
status = input('Input Stream active. Enter status report: ')
print(f'\n[STANDART] Archive report from {id}: {status}', file=sys.stdout)
print('[ALERT] System diagnostics: Comms channels verified', file=sys.stderr)
print('[STANDART] Data transmission complete', file=sys.stdout)
print('\n Three-channel communcation test successful.')
