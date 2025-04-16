from collections import deque

class Queue():
    """Simple queue to work with deque through 5th lab"""
    def __init__(self, data = []):
        self.items = deque(data)

    def __len__(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self) <= 0

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty(): return "queue is empty"
        else: return self.items.popleft()
    
    def appendleft(self, item):
        self.items.appendleft(item)
    
    def peek(self):
        if self.is_empty(): return "queue is empty"
        else: return self.items[0]


# from time import time
# from random import random
# if __name__ == '__main__':

#     start = time()
#     s1 = Stack()
#     for _ in range(100000):
#         s1.enqueue(random())
    
#     while not s1.is_empty():
#         s1.dequeue()
    
#     print(time() - start, s1.peek())