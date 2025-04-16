from simplestack import Stack
from sys import argv as entries

with open(entries[1], 'r', encoding='utf8') as f:
    operations = 0
    s1 = Stack()

    for line in f:
        code = line.strip('\n').split()
        if code[0] == 'push':
            s1.push(code[1])
        elif code[0] == 'pop':
            if s1.pop() == "stack is empty":
                break
        operations += 1

    print(operations, s1.peek())
