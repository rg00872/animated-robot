import random
def charge():
        global spam
        print('The power is too low. Recharging')
        print('Current power is (' + str(spam) + ')')
        #spam += 1
        return int(spam)

spam = random.randint(1,25)
print(' ***DEBUG*** ' + ' random number is ' + str(spam)) # DEBUG line for dev use!

while spam <= 20:
        spam = charge()
        spam += 1
        continue
print('The power has been recharged to adequate level ' + str(spam))
