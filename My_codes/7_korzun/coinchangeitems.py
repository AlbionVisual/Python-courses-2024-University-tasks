from sys import argv as entries

# entries = [1, '1,5,7', 10] # for debug

def greedy(noms, value, res):
    noms.sort(reverse=True)
    count = 0
    for coin in noms:
        res += [coin] * (value // coin)
        while value >= coin:
            value -= coin
            count += 1
    if value != 0: res.clear()
    return count if value == 0 else float('inf')

def dynamic(noms, value, res):
    res.clear()
    res_table = [[]] * (value + 1)
    table = [0] + [float('inf')] * (value + 1)
    for i in range(1, value + 1):
        for coin in noms:
            if i - coin >= 0: # fromula here
                if table[i] > table[i - coin] + 1:
                    table[i] = table[i - coin] + 1
                    res_table[i] = res_table[i - coin] + [coin]
    for el in res_table[-1]:
        res += [el]
    if table[value] == float('inf'): res.clear()
    return table[value]

noms = [int(x) for x in entries[1].split(',')]
value = int(entries[2])

res = []
print("greedy: ", greedy(noms, value, res), res)
print("dynamic:", dynamic(noms, value, res), res)