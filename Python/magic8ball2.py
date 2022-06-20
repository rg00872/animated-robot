import random

def getDay():
    global messages
    print(messages[random.randint(0, len(messages) - 1)])



messages = ['This is a Monday', \
    'This is a Tuesday', \
    'Thi is a Wednesday', \
    'This is a Thursday', \
    'This is a Friday', \
    'This is a Saturday', \
    'This is a Sunday']

#print(messages[random.randint(0, len(messages) - 1)])

getDay()