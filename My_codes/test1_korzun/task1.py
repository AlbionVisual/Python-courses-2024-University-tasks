def isDefferentDigits(number):
    s1 = str(number)
    s2 = str(number**2)
    return [int(i) for i in sorted(list(s1+s2))] == [1,2,3,4,5,6,7,8,9]

# числа меньшие 317 в квадрате дают число с меньше чем 6ю знаками
numbers = [i for i in range(300, 1000) if isDefferentDigits(i)]

print(numbers)