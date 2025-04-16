from time import time
from random import random
from collections import deque

class Stack():
    """Simple stack to work with deque through 5th lab"""
    def __init__(self, data = []):
        self.items = deque(data)

    def __len__(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self) <= 0
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty(): return "stack is empty"
        else: return self.items.pop()
    
    def peek(self):
        if self.is_empty(): return "stack is empty"
        else: return self.items[-1]

if __name__ == '__main__':

    start = time()
    s1 = Stack()
    for _ in range(100000):
        s1.push(random())
    
    while not s1.is_empty():
        s1.pop()
    
    print(time() - start, s1.peek())