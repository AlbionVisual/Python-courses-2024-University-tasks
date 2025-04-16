from simplestack import Stack
from sys import argv as entries

ops = entries[1].split()

stack = Stack()
err = False
for el in ops:
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
