def is_happy(n):
    digits = [int(x) for x in list(str(n))]
    digits = [0] * (6 - len(digits)) + digits
    return sum(digits[:3]) == sum(digits[3:])

print(len([x for x in range(1000000) if is_happy(x)]))