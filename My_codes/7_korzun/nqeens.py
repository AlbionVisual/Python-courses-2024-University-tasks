from sys import argv as entries
from time import time

def is_valid_solution(sol):                                 # Могут ли стоять так ферзи
    curr_row, curr_col = len(sol) - 1, sol[-1]
    
    for row in range(curr_row):
        if sol[row] == curr_col or abs(sol[row] - curr_col) == abs(row - curr_row):
            return False
    return True

def get_applicants(sol, n):                                 # Отбирает потенциально правильные решения и откидывает заведомо неверные
    applicants = []
    for col in range(n):
        if col not in sol:
            sol.append(col)
            if is_valid_solution(sol):
                applicants.append(col)
            sol.pop()
    return applicants

def search(sol, solutions, n):                              # Реккурсивная ф-ция
    if len(sol) == n:
        solutions.append(sol.copy())
        return

    for applicant in get_applicants(sol, n):                # Перебирает все возможные варианты избегая заведомо неверных
        sol.append(applicant)
        search(sol, solutions, n)
        sol.pop()

    
n = int(entries[1])

start = time()

solutions = []
sol = []
search(sol, solutions, n)


print(time() - start, len(solutions), solutions)