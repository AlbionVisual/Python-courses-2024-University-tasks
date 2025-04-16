import sys
import matplotlib.pyplot as plot

with open(sys.argv[1], 'r', encoding='utf8') as f:
                                                                    # Инициализация
    amounts = [0 for i in range(8)]
    f.readline()
    for line in f: 

        angle = int(line.split(',')[6])                             # Подсчёт кол-ва направлений ветра в определённую сторону
        for i in range(8):
            min = i * 45 - 22.5
            max = i * 45 + 22.5
            if angle > 337.5: angle -= 360
            if max >= 360: max -= 360
            if angle > min and angle < max: 
                amounts[i] += 1
                break
    
    amounts.append(amounts[0])

    vecs = [[0, 1],[2**(-1/2), 2**(-1/2)],[1, 0], [2**(-1/2), -2**(-1/2)], [0, -1], [-2**(-1/2), -2**(-1/2)], [-1, 0], [-2**(-1/2), 2**(-1/2)], [0, 1]]

    x = []; y = []
    for i in range(len(vecs)):                                      # Составление векторов
        x.append(vecs[i][0] * amounts[i])
        y.append(vecs[i][1] * amounts[i])
    
    plot.plot(x, y, 'b')

    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    textPosCoff = 1.3
    for i in range(len(x) - 1):
        plot.arrow(0, 0, x[i], y[i], head_width=3)                  # Конфигурации графика
        plot.text(vecs[i][0] * amounts[i] * textPosCoff - 2, vecs[i][1] * amounts[i] * textPosCoff - 2, directions[i], size='x-large')

    textPosCoff += 0.2
    plot.axis('equal')
    plot.grid(True)
    plot.title('Роза ветров Минска')
    left, right = plot.xlim()
    left *= textPosCoff; right *= textPosCoff
    if abs(left) > abs(right): plot.xlim((left, abs(left)))
    else: plot.xlim((-right, right))
    bottom, top = plot.ylim()                                       # Вывод графика
    bottom *= textPosCoff; top *= textPosCoff
    if abs(bottom) > abs(top): plot.xlim((bottom, abs(bottom)))
    else: plot.ylim((-top, top))
    plot.show()