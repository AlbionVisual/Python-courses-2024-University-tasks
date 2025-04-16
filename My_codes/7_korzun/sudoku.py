from sys import argv as entries
from time import time

def print_board(board):                         # Вывод досок
    print("+---+---+---+")
    for i in range(9):
        print(f'|{"".join(str(cell) if cell != 0 else "*" for cell in board[i][0:3])}|'
              f'{"".join(str(cell) if cell != 0 else "*" for cell in board[i][3:6])}|'
              f'{"".join(str(cell) if cell != 0 else "*" for cell in board[i][6:9])}|')
        if i % 3 == 2: print("+---+---+---+")

def is_safe(board, row, col, num):              # Проверяем можно ли вставить число в клетку
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    
    for i in range(3):
        for j in range(3):
            if board[i + row - row % 3][j + col - col % 3] == num:
                return False
    return True

def solve_sudoku(board):                        # Реккурсивная ф-ция
    empty_pos = first_empty(board)
    if not empty_pos:
        return [board]
    row, col = empty_pos

    solutions = []
    for num in range(1, 10):
        if is_safe(board, row, col, num):       # Реккурсия
            board[row][col] = num
            for solution in solve_sudoku(board):
                solutions.append([row[:] for row in solution])
            board[row][col] = 0
    return solutions

def first_empty(board):                         # Ищет первую пустую клетку
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


with open(entries[1], 'r') as f:
    board = []
    for line in f:
        board.append([int(char) if char.isdigit() else 0 for char in line.strip()])

print_board(board)

start = time()
solutions = solve_sudoku(board)

print(f"{len(solutions)} solutions found in {time() - start} seconds\n")

for i, solution in enumerate(solutions):
    print(f"Solution # {i}")
    print_board(solution)