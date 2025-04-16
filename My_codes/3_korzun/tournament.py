import sys

def sort(matr, id1, id2):                                       # Сортировка матрицы по двум столбцам

    n = len(matr[0])

    for i in range(n - 1):
        maxId = i

        for j in range(i + 1, n):
            if matr[id1][j] > matr[id1][maxId]:                 # Поиском максимального
                maxId = j
            elif matr[id1][j] == matr[id1][maxId] and matr[id2][j] > matr[id2][maxId]:
                maxId = j
        for j in range(len(matr)):                              # А здесь маняем местами
            matr[j][i], matr[j][maxId] = matr[j][maxId], matr[j][i]

    return matr


players, games, won, drawn, lost, score, sb = [], [], [], [], [], [], []

with open(sys.argv[1], 'r', encoding='utf8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        for i in range(2):

            if line[i] not in players:
                players.append(line[i])
                games.append(0)
                score.append(0)
                won.append(0)                                   # Обработка входных данных
                drawn.append(0)
                lost.append(0)
                sb.append(0)

            id = players.index(line[i])
            games[id] += 1
            score[id] += float(line[i + 2])
            won[id] += 1 if float(line[i + 2]) == 1.0 else 0    # Сразу считаем некоторые значения
            drawn[id] += 1 if float(line[i + 2]) == 0.5 else 0
            lost[id] += 1 if float(line[i + 2]) == 0.0 else 0

    f.seek(0)
    for line in f:
        line = line.strip('\n').split('\t')

        id1 = players.index(line[0])
        cof1, cof2 = float(line[2]), float(line[3])             # Читаем второй раз для подсчёта суммы SB
        id2 = players.index(line[1])

        sb[id1] += score[id2] * cof1
        sb[id2] += score[id1] * cof2

    [players, games, won, drawn, lost, score, sb] = sort([players, games, won, drawn, lost, score, sb], 5, 6)

    print("#\tName\t\tGames\tWon\tDrawn\tLost\tScore\tSB")
    for i in range(len(players)):
        tb = '\t'                                               # Вывод
        print(f'{i + 1}\t{players[i]}{tb+tb if len(players[i]) < 8 else tb}{games[i]}\t{won[i]}\t{drawn[i]}\t{lost[i]}\t{score[i]}\t{sb[i]}')