def getAge():
    while True:
        print('What is your age ?')
        input_age = input()
        if input_age.isdecimal():
            break
        else:
            print('Please enter anumber for your age.')
    return input_age

def getpW():
    while True:
        print('Enter a password:')
        input_pw = input()
        if input_pw.isalnum():
            break
        else:
            print('Only numbers and letters are allowed for password.')
    return input_pw

age = int(getAge())
if age > 17:
    print('Your age is ' + str(age))
else:
    print(str(age) + ' is too young. Come back next year!')