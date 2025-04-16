import sys
# import time
import random

# start = time.time()

def isUnReapeted(num):                                  # Проверяет есть ли повторяющиеся цифры
    digits = list(str(num))
    for i in range(len(digits)-1):
        if digits[i] == '0': return False
        for j in range(i + 1, len(digits)):
            if digits[i] == digits[j]:
                return False
    return True

def cows(num, guess):                                   # Считает кол-во коров
    amount = 0
    num = list(str(num))
    guess = list(str(guess))

    for i in range(len(num)):
        for j in range(len(guess)):
            if i == j: continue
            if num[i] == guess[j]: amount += 1

    return amount

def bulls(num, guess):                                  # Считает кол-во быков
    amount = 0
    num = list(str(num))
    guess = list(str(guess).zfill(len(num)))

    for i in range(len(num)):
        if num[i] == guess[i]: amount += 1

    return amount
    

amount = 4 if len(sys.argv) == 1 else int(sys.argv[1])
                                                        # Инициализация
numbers = [i for i in range(10**(amount - 1), 10**amount) if isUnReapeted(i)]

number = numbers[random.randint(0, len(numbers) - 1)]
print(f'Number: {number}')                              # Число для поиска

guess = -1

while number != guess:
    
                                                        # 1 ход по алгоритму
    guess = numbers[random.randint(0, len(numbers) - 1)]
    amounts = [bulls(number, guess), cows(number, guess)]
    print(f'Guess = {guess}, (Bulls, Cows) = ({amounts[0]}, {amounts[1]})')
    if number != guess: print(f'Candidates ({len(numbers)}): {numbers[:10]}\n')
    else:
        numbers = [guess]
        print(f'Candidates ({len(numbers)}): {numbers[:10]}\n')
        break
    numbers = [i for i in numbers if amounts[0] == bulls(i, guess) and amounts[1] == cows(i, guess)]


# print(guess)

# print(time.time() - start)

# while number != guess:
    
#                                                         # 1 ход по алгоритму
#     guess = numbers[random.randint(0, len(numbers) - 1)]
#     amounts = [bulls(number, guess), cows(number, guess)]
#     print(f'Guess = {guess}, (Bulls, Cows) = ({amounts[0]}, {amounts[1]})')
#     
#     print(f'Candidates ({len(numbers)}): {numbers[:10]}\n')
#     numbers = [i for i in numbers if amounts[0] == bulls(i, guess) and amounts[1] == cows(i, guess)]
