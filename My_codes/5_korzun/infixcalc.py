from sys import argv as entries
from simplestack import Stack

ops = Stack()
res = []
err = False
line = entries[1].split()

for el in line:
    if el.isdigit(): res += [el]
    elif el == '(': ops.push(el)
    elif el == ')':
        ex = ops.pop()
        while ex != '(':
            if ex == 'stack is empty': 
                err = 'invalid input'
                break
            res += [ex]
            ex = ops.pop()
        if err: break
    elif el in '+-':
        while ops.peek() != '(' and ops.peek() != 'stack is empty':
            res += [ops.pop()]
        ops.push(el)
    elif el in '*/':
        while ops.peek() == '*' or ops.peek() == '/':
            res += [ops.pop()]
        ops.push(el)
    else:
        err = 'invalid input'
        break

while not ops.is_empty():
    res += [ops.pop()]

if not err:
    stack = Stack()
    for el in res:
        if el.isdigit():
            stack.push(int(el))
        else:
            b = stack.pop()
            a = stack.pop()
            if type(a) != str and type(b) != str:
                if el == '+':
                    stack.push(a + b)
                elif el == '-':
                    stack.push(a - b)
                elif el == '*':
                    stack.push(a * b)
                elif el == '/':
                    if b == 0: 
                        err = 'division by zero'
                        break
                    else:
                        stack.push(a / b)
                else: 
                    err = 'invalid input'
                    break
            else:
                err = 'invalid input'
                break

print(err if err else stack.peek())
