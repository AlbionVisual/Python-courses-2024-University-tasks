from sys import argv as entries
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def is_valid_move(maze, pos):                   # Проверка находятся ли координаты внутри поля и нет ли стены
    return maze[pos[0]][pos[1]] == ' ' and (0 <= pos[0] and pos[0] < len(maze)) and (0 <= pos[1] and pos[1] < len(maze[0]))

def get_neighbors(maze, pos):                   # Проверяет всех соседей
    neighbors = [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]
    return [neighbor for neighbor in neighbors if is_valid_move(maze, neighbor)]

def search(maze, current, end, path):           # Реккурсивная ф-ция перебора вариантов
    if current == end:                          # Если нашли путь останавливаем реккурсию
        path.append(current)
        return True
    if not is_valid_move(maze, current):
        return False

    maze[current[0]][current[1]] = '2'                            # Отмечаем посещенную ячейку
    
    for neighbor in get_neighbors(maze, current):
        if search(maze, neighbor, end, path):   # Реккурсия, пока не наткнёмся на точку end или пока не закончатся варианты
            path.append(current)
            return True
    
    return False





start = tuple([int(i) for i in entries[2].split(',')])
end = tuple([int(i) for i in entries[3].split(',')])

with open(entries[1], 'r') as file:
    maze = [list(line.strip()) for line in file]

path = []
if search(maze, start, end, path):
    path.reverse()
    print(len(path), path)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == '1':
                ax.add_patch(patches.Rectangle((x, len(maze) - y - 1), 1, 1, facecolor='black'))
            elif (y, x) in path:
                ax.add_patch(patches.Rectangle((x, len(maze) - y - 1), 1, 1, facecolor='red'))

    plt.xlim(0, len(maze[0]))
    plt.ylim(0, len(maze))
    plt.show()
else:
    print("No path exists!")



