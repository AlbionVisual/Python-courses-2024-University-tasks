import sys

abc = 'abcdefghijklmnopqrstuvwxyz'
chars = []
counts = []

with open(sys.argv[1], 'r', encoding='utf8') as f:

    for line in f:
        for ch in line.lower():
            if ch in abc:
                if ch in chars:
                    counts[chars.index(ch)] += 1
                else:
                    chars += [ch]
                    counts += [1]

    for i in range(len(counts)):
        for j in range(i, len(counts)):
            if counts[i] < counts[j]:
                counts[i], counts[j] = counts[j], counts[i]
                chars[i], chars[j] = chars[j], chars[i]

    for i in range(len(counts)):
        print(f'{chars[i]}\t{counts[i]}')