from collections import deque
import random
import time

class Stack:
    def __init__(self):
        self.items = deque()
    def create_stack(self):
        
        return Stack()
    def is_empty(self):
        """Проверяет, пуст ли стек (возвращает True, если пуст, иначе False)."""
        return len(self.items) == 0

    def push(self, item):
       
        self.items.append(item)

    def pop(self):
        
        if not self.is_empty():
            return self.items.pop()
        else:
            print("stack is empty")

    def peek(self):
    
        if not self.is_empty():
            return self.items[-1]
        else:
            print("stack is empty")

if __name__ == "__main__":
    stack = Stack()
    start_time = time.time()

    # Добавляем 100 тыс. случайных чисел от 0 до 1 в стек
    for _ in range(100000):
        stack.push(random.random())

    # Извлекаем элементы из стека, пока он не станет пустым
    while not stack.is_empty():
        stack.pop()

    end_time = time.time()
    time = end_time - start_time

    if stack.is_empty():
        print(time, "stack is empty")
    else:
        print(time, stack.peek())

