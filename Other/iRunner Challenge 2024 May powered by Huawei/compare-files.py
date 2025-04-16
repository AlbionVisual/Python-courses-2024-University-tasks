from sys import argv as entries

out = open(entries[1], 'r', encoding='utf8')
ans = open(entries[2], 'r', encoding='utf8')

failed = []
amount = 0


for outline in out:
    amount += 1
    ansline = ans.readline().strip('\n').split()
    outline = outline.strip('\n').split()
    for i in range(3):
        if round(float(ansline[i]), 4) != round(float(outline[i]), 4):
            failed += [(amount, ' '.join(outline), ' '.join(ansline))]
            break

ans.close()
out.close()

for line in failed:
    print(line[0], ': ', line[1], ' != ', line[2])

print(f'Failed: {len(failed)}, out of: {amount}, that is: {round(len(failed) / amount * 100, 1)}%')