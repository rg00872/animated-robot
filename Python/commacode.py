def assignComma(things):
    new_string = ''
    for i in range(len(things) - 1):
        new_string += things[i] + ', '
    
    #new_string += 'and ' + things[-1]
    print(new_string)

dogs = ['pit', 'yorkie', 'terrier', 'poodle']

assignComma(dogs)