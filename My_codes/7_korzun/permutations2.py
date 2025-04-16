from sys import argv as entries

def is_valid_solution(sol, n):                                 # Функция проверки на валидность
    return len(sol) == n

def search(sol, solutions, string, n):                             # Реккурсивная функция для проверки всех возможных значений
    if is_valid_solution(sol, n):
        solutions.append(sol.copy())

    for sym in [el for el in string if el not in sol]:    # Посимвольный перебор со вставкой в тест
        sol.append(sym)
        search(sol, solutions, string, n)
        sol.pop()

n = len(entries[1])
string = list(entries[1])

solutions = []
sol = []
search(sol, solutions, string, n)

print(len(solutions), [''.join(i) for i in solutions])