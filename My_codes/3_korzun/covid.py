import sys, matplotlib.pyplot as plt

filter = '' if len(sys.argv) <= 3 else sys.argv[3].lower()          # Ввод или значения по умолчанию
n = 11 if len(sys.argv) <= 2 else int(sys.argv[2])

with open(sys.argv[1], 'r', encoding='utf8') as f:

    countries = []
    amounts = []
    sum = 0
    name = ''

    for line in f:                                                  # Ввод и обработка
        stats = line.strip('\n ').split(',')
        if filter in stats[1].lower() and stats[n] != '' and stats[1] != 'continent' and stats[1] != '':
            countries.append(stats[2])
            amounts.append(float(stats[n]))
            sum += float(stats[n])
        if stats[1] == 'continent': name = stats[n]

    avg = sum / len(amounts)
    
    sum = 0
    for i in amounts:                                               # Подсчёт значений для грфика
        sum += (i - avg)**2
    dev = (sum / (len(amounts) - 1))**(1/2)

    x = []; y = []
    above = []
    below = []
    for i in range(len(amounts)):
        x.append(i)
        y.append(amounts[i])
        if amounts[i] > avg + dev:                                  # Переменные для графиков
            above.append(f'{countries[i]}: {int(amounts[i])}')
        elif amounts[i] < avg - dev:
            below.append(f'{countries[i]}: {int(amounts[i])}')

    fig, (ax1, ax2) = plt.subplots(1, 2, gridspec_kw={'width_ratios':[3,1]})
    ax1.scatter(x, y, s=2)
    ax1.plot([0, x[-1]], [avg, avg], 'r')
    ax1.plot([0, x[-1]], [avg + dev, avg + dev], 'b--')
    ax1.plot([0, x[-1]], [avg - dev, avg - dev], 'b--')
    ax2.axis(False)
    newLine = '\n'                                                  # Вывод графика
    form = '{:.2f}'
    ax2.text(0, 1, f'{name}\n\nMean: {form.format(avg)}\nSt. dev:[{form.format(avg - dev)},{form.format(avg + dev)}]\n\nToo high:\n{newLine.join(above)}\n\nToo low:\n{newLine.join(below)}', fontsize=8, verticalalignment='top')
    plt.show()

