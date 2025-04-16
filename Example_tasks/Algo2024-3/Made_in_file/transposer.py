import sys

f = open(sys.argv[1], 'r', encoding='utf8')
m = [[int(num) for num in line.strip('\n').split('\t')] for line in f]
f.close()

rows = len(m[0])
cols = len(m)
mt = [[0]*cols for i in range(rows)]

for i in range(cols):
    for j in range(rows):
        mt[j][i] = m[i][j]

f = open('mt.tsv', 'w')
f.write('\n'.join(['\t'.join([str(num) for num in line]) for line in mt]))
f.close()