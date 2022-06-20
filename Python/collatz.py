def collatz(number): # collatz function
        if number % 2 == 0: # condition for even number
            print(number // 2)
            return number // 2

        elif number % 2 == 1: # condition for odd number
            print(3 * number + 1)
            return 3 * number + 1

print('Please enter a number') # Prompt the user for a integer

# Error handling invalid data
try:
    userEntry = int(input())
    while userEntry != 1:
        userEntry = collatz(userEntry)

except ValueError:
    print('You did not enter a number.')

