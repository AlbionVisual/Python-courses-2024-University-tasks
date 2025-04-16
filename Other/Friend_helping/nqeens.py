import time
import sys

def is_safe(board, row, col):
    # Проверяем, что нет ферзей на одной вертикали
    for i in range(row):
        if board[i] == col:
            return False

    # Проверяем, что нет ферзей на одной диагонали
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve_nqueens(n):
    solutions = []
    board = [-1] * n  # Инициализируем доску

    def backtrack(row):
        nonlocal solutions
        if row == n:  # Базовый случай: достигнут конец доски
            solutions.append(list(board))  # Добавляем решение в список
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Размещаем ферзя на доске
                backtrack(row + 1)  # Рекурсивно переходим к следующей строке

    start_time = time.time()
    backtrack(0)  # Начинаем с первой строки
    end_time = time.time()
    elapsed_time = end_time - start_time
    num_solutions = len(solutions)

    return elapsed_time, num_solutions, solutions

n = int(sys.argv[1])
elapsed_time, num_solutions, solutions = solve_nqueens(n)

print(elapsed_time, num_solutions, solutions)