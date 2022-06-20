spam = 0
while spam < 5:
    print("Hello World!" + str(spam))
    spam = spam + 1
    break
print("we're done here")
if spam <= 4:
    print("your int " + str(spam) + " is too low, come back later !")
