import sys

str, divider = str(sys.argv[1]), str(sys.argv[2])

str, divider = str.lower(), divider.lower()

def countAmount(string, divide):
    count = 0
    id = 0
    for i in string:
        if i == divide[id]:
            id += 1
            if id >= len(divide):
                id = 0
                count += 1
    return count

print(countAmount(str,divider))
