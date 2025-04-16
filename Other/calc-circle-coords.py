from sys import argv as entries
from pprint import pprint as print
import matplotlib.pyplot as plot
import numpy as np

center = tuple(int(i) for i in entries[2:4])
radius = int(entries[1])
step = np.pi / 400

# print([radius, center])

circle = set()
circle2 = []

stage_x = 0

out = open('output_dists.txt', 'w', encoding='utf8')

for i in np.arange(0, 2 * np.pi, step):
    
    coord = (int(center[0] + radius * np.cos(i)), int(center[0] + radius * np.sin(i)))

    if coord not in circle2:
        if len(circle2) > 1:
            if coord[0] == circle2[-1][0]: stage_x += 1
            else: 
                if coord[0] > circle2[-1][0]: stage_x *= -1
                out.write(str(stage_x) + ' ')
                stage_x = 0
        circle2 += [coord]

    circle.add(coord)

out.close()

cords = np.array(list(circle))

# plot.plot(cords[:,0], cords[:,1], 'ro')
# plot.show()

with open('output_cords.txt', 'w', encoding='utf8') as f:
    for i in circle:
        f.write(str(i) + '\n')
        # print(i)