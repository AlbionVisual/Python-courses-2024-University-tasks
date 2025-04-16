import sys

a = 3 if len(sys.argv) == 2 else int(sys.argv[2])               # Ввод параметров относительно их кол-ва
b = a if len(sys.argv) == 3 or len(sys.argv) == 2 else int(sys.argv[3])

with open(sys.argv[1], 'r', encoding="utf8") as f:

    words = []

    for line in f:
        # Better filter:
        # line = line.replace('"', ' ').replace('.', ' ').replace(',', ' ').replace('?', ' ').replace(':', ' ').replace(';', ' ').replace('\n', ' ').replace('\t', ' ').replace('!', ' ').replace('§', ' ').replace('(', ' ').replace(')', ' ').replace('-', ' ')
        for word in line.split():                               # Разрезаем строки на слова и кострируем их
            if word.strip("?!-\",;.:‡§()§'").lower() != '': # .,\"!\n?\t:;-‡§( )§ <- use this with better filter
                words.append(word.strip("?!-\",;.:‡§()§'").lower())

    words = sorted(words)                                       # Сортируем для алгоритма

    condidates = []
    amounts = []
    i = 0
    while i < len(words):
        word = words[i]
        if len(word) >= a and len(word) <= b:                   # Обрабатываем каждое слово и вставляем в список кандидатов
            condidates.append(word)
            amounts.append(0)
            while word == condidates[-1]:
                amounts[-1] += 1
                if i < len(words) - 1:
                    i += 1
                else: break
                word = words[i]
        i += 1

    for i in range(10):                                         # Перемещаем сортировкой в конец 10 элементов

        isInRow = True
        for j in range(i, len(condidates) - 1):
            if amounts[j] > amounts[j + 1]:                     # "Эффективная" сортировка пузырьком
                isInRow = False
                amounts[j], amounts[j + 1] = amounts[j + 1], amounts[j]
                condidates[j], condidates[j + 1] = condidates[j + 1], condidates[j]
        if isInRow: break

    for i in range(1, 11):
        print(amounts[-i], condidates[-i])                      # Вывод
