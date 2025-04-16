import sys, matplotlib.pyplot as plt

# import time
# start = time.time()

def firstDigit(num):                                            # Поиск первой цифры
    while num // 10 != 0:
        num /= 10
    return int(num)

filter = '' if len(sys.argv) < 3 else sys.argv[2].lower()
digits = [0] * 9                                                # Инициализация
amounts = [0] * 9

with open(sys.argv[1], 'r', encoding='utf8') as f:

    names = f.readline()

    if filter != '':                                            # Ввод и обработка без фильтра

        countries = [i.lower() for i in names.strip('\n ').split(',')]
        n = countries.index(filter)

        for line in f:
            num = line.strip('\n ').split(',')[n]
            if num != '0.0' and num != '':
                num = int(float(num))
                digits[firstDigit(num) - 1] += 1
                amounts[firstDigit(num) - 1] += 1
        
    else:                                                       # Сложные ввод и обработка
        for line in f:
            stats = line.strip('\n ').split(',')
            for i in stats[1:]:
                if i != '0.0' and i != '':
                    i = int(float(i))
                    digits[firstDigit(i) - 1] += 1
                    amounts[firstDigit(i) - 1] += 1



fig, ax = plt.subplots()                                        # Вывод графика

x = [i for i in range(1, 10)]

print([[x[i], amounts[i], int(amounts[i] / sum(amounts) * 10000 + 0.5) / 100.0] for i in range(len(x))])

ax.bar(x, digits)

# print(time.time() - start)

plt.show()