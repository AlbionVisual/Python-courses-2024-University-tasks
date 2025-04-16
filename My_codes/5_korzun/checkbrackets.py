from simplestack import Stack
from sys import argv as entries


entries[1] = entries[1].replace(' ', '')

def checkbrackets(s):
    stack = Stack()
    for el in s:
        if el == '(':
            stack.push('(')
        elif el == ')':
            if stack.pop() == '(':
                continue
            else: return False
    return True if stack.is_empty() else False


print(checkbrackets(entries[1]))