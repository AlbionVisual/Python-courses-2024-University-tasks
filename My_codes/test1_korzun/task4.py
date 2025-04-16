import sys

symAmount = int(sys.argv[2])

lines = []

with open(sys.argv[1], 'r', encoding='utf8') as f:
    for line in f:

        line = [i for i in line.strip('\n').split(' ') if i != '']

        lettersAmount = sum([len(i.strip(' ')) for i in line if i != ''])
        delta = symAmount - lettersAmount
        l = len(line) - 1

        spaces = delta // l if l != 0 else 0
        rest = delta % l

        lines.append((' '*(spaces+1)).join(line[:rest]) + (' '*(spaces + 1) if rest != 0 else '') + (' '*spaces).join(line[rest:]))

with open(sys.argv[1], 'w', encoding='utf8') as f:
    for i in lines:
        f.write(i + '\n')