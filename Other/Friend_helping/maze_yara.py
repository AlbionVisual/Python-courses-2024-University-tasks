import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def create_maze(width, height):
    """
    Создает лабиринт с использованием модифицированного алгоритма Прима.
    
    Args:
        width (int): Ширина лабиринта.
        height (int): Высота лабиринта.
        
    Returns:
        list: Матрица лабиринта.
    """
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    # Выбираем случайную начальную клетку
    start_row = random.randint(0, height - 1)
    start_col = random.randint(0, width - 1)
    maze[start_row][start_col] = 0
    
    # Список клеток, которые нужно обработать
    cells_to_process = [(start_row, start_col)]
    
    while cells_to_process:
        # Выбираем случайную клетку из списка
        row, col = random.choice(cells_to_process)
        cells_to_process.remove((row, col))
        
        # Находим соседние клетки
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        random.shuffle(neighbors)
        
        for neighbor_row, neighbor_col in neighbors:
            if 0 <= neighbor_row < height and 0 <= neighbor_col < width and maze[neighbor_row][neighbor_col] == 1:
                maze[neighbor_row][neighbor_col] = 0
                cells_to_process.append((neighbor_row, neighbor_col))
    
    return maze

def display_maze(maze):
    """
    Выводит лабиринт в матричном и графическом виде.
    
    Args:
        maze (list): Матрица лабиринта.
    """
    width, height = len(maze[0]), len(maze)
    
    # Вывод в матричном виде
    print("Матрица лабиринта:")
    for row in maze:
        print(" ".join(map(str, row)))
    
    # Вывод в графическом виде
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    
    for row in range(height):
        for col in range(width):
            if maze[row][col] == 1:
                ax.add_patch(Rectangle((col, height - row - 1), 1, 1, facecolor='black'))
    
    plt.show()

# Пример использования
width, height = 15, 15
maze = create_maze(width, height)
display_maze(maze)
