import sys

with open(sys.argv[1], 'r', encoding='utf8') as f:

    word_to_find = sys.argv[2]

    k = 0
    for line in f:
        for word in line.lower().split():
            if word == word_to_find:
                k += 1
    print(k)