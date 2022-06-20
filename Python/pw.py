#! python3
# This program will be a prototype password locker
# pw.py - an insecure password locker program.
PASSWORDS = {'email': 'F492ji93jj93ndHSM97KNH', 'blog': 'VLSMKS98837KSjhjsn', 'luggage':'33985'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no accont named ' + account)