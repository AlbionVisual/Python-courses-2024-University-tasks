import sys

sys.argv.append('F:\\University\\Python\\Example_tasks\\Algo2024-3\\tata2024.tsv')

names, games, wins, drawns, loses, scores, burger = [], [], [], [], [], [], []
tata = []
def change(mas, a, b):
    for i in range(len(mas)):
        mas[i][a], mas[i][b] = mas[i][b], mas[i][a]
with open(sys.argv[1], 'r', encoding='utf8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        tata.append(line)
    for line in tata:
        if line[0] not in names:
            names.append(line[0])
            games.append(0)
            scores.append(0)
            wins.append(0)
            drawns.append(0)
            loses.append(0)
            burger.append(0)
        ind = names.index(line[0])
        games[ind] += 1
        scores[ind] += float(line[2])
        if float(line[2]) == 1.0:
            wins[ind] += 1
        elif float(line[2]) == 0.5:
            drawns[ind] += 1
        else:
            loses[ind] += 1
        if line[1] not in names:
            names.append(line[1])
            games.append(0)
            scores.append(0)
            wins.append(0)
            drawns.append(0)
            loses.append(0)
            burger.append(0)
        ind = names.index(line[1])
        games[ind] += 1
        scores[ind] += float(line[3])
        if float(line[3]) == 1.0:
            wins[ind] += 1
        elif float(line[3]) == 0.5:
            drawns[ind] += 1
        else:
            loses[ind] += 1
    for line in tata:
        a = names.index(line[0])
        b = names.index(line[1])
        if line[2] == '1':
            burger[a] += scores[b]
        elif line[2] == '0.5':
            burger[a] += scores[b] / 2
            burger[b] += scores[a] / 2
        else:
            burger[b] += scores[a]
    mas = [names, games, wins, drawns, loses, scores, burger]
    n = len(mas[0])
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if mas[5][j] < mas[5][j + 1]:
                change(mas, j, j+1)
            elif mas[5][j] == mas[5][j + 1] and mas[6][j] < mas[6][j + 1]:
                change(mas, j, j+1)
        # for j in range(len(mas)):
        #     mas[j][i], mas[j][j + 1] = mas[j][j + 1], mas[j][i]
    [names, games, wins, drawns, loses, scores, burger] = mas
    print("#\tName\t\tGames\twins\tdrawns\tloses\tscores\taburger")
    for i in range(len(names)):
        tab = '\t'
        print(f'{i + 1}\t{names[i]}{tab+tab if len(names[i]) < 8 else tab}{games[i]}\t{wins[i]}\t{drawns[i]}\t{loses[i]}\t{scores[i]}\t{burger[i]}')