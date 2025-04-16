from sys import argv as entries

def greedy(noms, value):
    noms.sort(reverse=True)
    count = 0
    for coin in noms:
        while value >= coin:
            value -= coin
            count += 1
    return count if value == 0 else float('inf')

def dynamic(noms, value):
    table = [0] + [float('inf')] * (value + 1)
    for i in range(1, value + 1):
        for coin in noms:
            if i - coin >= 0:
                if table[i] > table[i - coin] + 1:
                    table[i] = table[i - coin] + 1
    return table[value]

noms = [int(x) for x in entries[1].split(',')]
value = int(entries[2])

print("greedy: ", greedy(noms, value))
print("dynamic:", dynamic(noms, value))