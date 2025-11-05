#! python3
# main.py - An insecure password locker program.

PASSWORDS = {
            'email': 'sdwqvdtds!@#!@SADd',
            'ryanair': 'ryanaaairr22',
            'youtube': 'ilikecats3009'
            }

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python main.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}')