import sys

def isYear(s):                                                  # Проверка все ли числа в строке
    for i in list(s):
        if i < '0' or i > '9':
            return False
    return True

f = open(sys.argv[1], 'r', encoding='utf8')

country = '*'
year = 2024                                                     # Значения по умолчанию

if len(sys.argv) == 3:
    if isYear(sys.argv[2]): year = int(sys.argv[2])             # Если ввели 1 фильтр
    else: country = sys.argv[2]
if len(sys.argv) == 4:
    year = sys.argv[2] if isYear(sys.argv[2]) else sys.argv[3]  # Если ввели 2 фильра
    year = int(year)
    country = sys.argv[2].lower() if not isYear(sys.argv[2]) else sys.argv[3].lower()

year -= 71                                                      # Год на который мы проверяем

for line in f:
    line = line.strip('\n').split('\t')                         # Если год указан в году смерти, вывести
    if line[2] != 'death' and line[2] != '*' and int(line[2]) == year and (country == '*' or country in line[3].lower()):
        print(f'{line[0]} ({line[1]}-{line[2]}) {line[3]}')

f.close()
