import sys, random

n = int(sys.argv[1])

print(f'I\'ve thougth of a number beetween 0 and {n}. Guess it.')

trials = 1
guess = n // 2
while True:
    try:
        hint = int(input(f'\nNumber {guess}? (0 if your number is less, 1 if is greater, 2 if I win): '))

        if (hint == 0):
            trials += 1
            guess -= n // 2**trials + 1
        elif (hint == 1):
            trials += 1
            guess += n // 2**trials + 1
        else:
            print(f'\nYes, it\'s {guess}! It took {trials}')
            break
    except ValueError:
        print(f'Error: it\'s not a number.')
    except:
        print(f'Error: something went wrong.')