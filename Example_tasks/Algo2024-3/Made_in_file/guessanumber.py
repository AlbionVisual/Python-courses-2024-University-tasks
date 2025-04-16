import sys, random

n = int(sys.argv[1])
r = random.randrange(n+1)

print(f'I\'ve thougth of a number beetween 0 and {n}. Guess it.')

trials = 0

while True:
    try:
        guess = int(input(f'\nEnter your guess: '))
        trials += 1
        if (guess > r):
            print(f'My number is less than {guess}.')
        elif (guess < r):
            print(f'My number is greater that {guess}.')
        else:
            print(f'\nYes, it\'s {guess}! It took {trials}')
            break
    except ValueError:
        print(f'Error: it\'s not a number.')
    except:
        print(f'Error: something went wrong.')