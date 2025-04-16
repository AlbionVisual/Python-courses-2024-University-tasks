from sys import argv as entries

with open(entries[1], 'r', encoding='utf8') as f:
    table = []
    for line in f:
        table += [line.strip('\n')]
    isValid = True
    for i1 in range(3):
        if isValid:
            for j1 in range(3):
                s = set()
                count = 0
                for i2 in range(3):
                    for j2 in range(3):
                        cell = table[i1 * 3 + i2][j1 * 3 + j2]
                        if cell != '*':
                            count += 1
                            s.add(cell)
                if len(s) < count: 
                    isValid = False
                    break
    
    if isValid:
        for i in range(9):
            if isValid:
                count1 = count2 = 0
                s1 = set()
                s2 = set()
                for j in range(9):
                    if table[i][j] != '*':
                        count1 += 1
                        s1.add(table[i][j])
                    if table[j][i] != '*':
                        count2 += 1
                        s2.add(table[j][i])
                if len(s1) < count1:
                    isValid = False
                    break
                if len(s2) < count2:
                    isValid = False
                    break
    
    print(isValid)