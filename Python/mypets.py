myPets = ['Zophie', 'Pooka', 'Fat-tail']

while True:
    print('enter a petname')
    name = input()

    if name not in myPets:
        print('We do not have a pet named ' + name + '. Please try again')
        continue
    else:
        print(name + ' is my pet.')
        break
print('Thanks! ' + name + ' is ready to be picked up' )
