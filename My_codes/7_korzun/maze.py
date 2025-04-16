from random import randrange
from random import choice
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sys import argv as entries


def get_neighbours(cell, width, height):                    # Вычисление координат соседей
    neighbours = []
    vecs = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    
    for direction in vecs:
        if 0 <= cell[0] + direction[0] < height and 0 <= cell[1] + direction[1] < width:
            neighbours.append((cell[0] + direction[0], cell[1] + direction[1]))
    
    return neighbours


def create_maze(width, height):                             # Создание лабиринта
    field = [[1 for _ in range(width)] for _ in range(height)]
    
    start_y, start_x = randrange(1, height, 2), randrange(1, width, 2)
    field[start_y][start_x] = 0
    
    suspicios = get_neighbours((start_y, start_x), width, height)
    
    while suspicios:
        curr = choice(suspicios)
        suspicios.remove(curr)
        
        neighbours = get_neighbours(curr, width, height)
        filtered = [n for n in neighbours if field[n[0]][n[1]] == 0]
        
        if filtered:
            neighbour = choice(filtered)
            between = ((curr[0] + neighbour[0]) // 2, (curr[1] + neighbour[1]) // 2)
            
            field[curr[0]][curr[1]] = 0
            field[between[0]][between[1]] = 0
            
            new_suspicios = neighbours
            for new in new_suspicios:
                if field[new[0]][new[1]] == 1 and new not in suspicios:
                    suspicios.append(new)
    
    return field   



width = int(entries[1])
height = int(entries[2])

maze = create_maze(width, height)

for row in maze:                                            # Вывод матрицы
    print(''.join('1' if cell == 1 else ' ' for cell in row))

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xticks([])                                           # Отрисовка матрицы
ax.set_yticks([])

for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == 1:
            ax.add_patch(patches.Rectangle((x, len(maze) - y - 1), 1, 1, edgecolor='black', facecolor='black'))

plt.xlim(0, len(maze[0]))
plt.ylim(0, len(maze))
plt.show()