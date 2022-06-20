def getNumber(name):
     global luckyNumber
     if name in luckyNumber:
        print(str(luckyNumber[name]) + ' is the lucky number of ' + name )
     else:
        try:
             print(name + ' has no information registered.')
             print('Enter a number for ' + name)
             numEntry = int(input())
             luckyNumber[name] = numEntry
             print(name + ' has been registered.')
        except ValueError:
            print('Please enter a valid number')


luckyNumber = {'Jody': 1, "Herald": 10, "Fave": 3, "Gerald": 8, "Benny": 23}

while True:
    print('Enter a name for lookup: (Enter blank to exit)')
    userEntry = input()
    if userEntry == '':
        break
    getNumber(userEntry)