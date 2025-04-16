class MinHeap:
    
    def __init__(self, arr = []):
        self.items = []
        for i in arr: self.push(i)
    
    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self) <= 0

    def peek(self):
        if self.is_empty(): return 'heap is empty'
        else: return self.items[0]
    
    def push(self, item):
        self.items += [item]
        self.sift_up(len(self) - 1)

    def pop(self):
        if len(self) != 0:
            self.items[0], self.items[-1] = self.items[-1], self.items[0]
            popped = self.items.pop()
            self.sift_down(0)
            return popped
        else: return 'heap is empty'

    def get_data(self):
        return self.items
    
    def sift_up(self, i):
        while i >= 1 and self.items[i] < self.items[(i-1)//2]:
            self.items[i], self.items[(i-1)//2] = self.items[(i-1)//2], self.items[i]
            i = (i-1)//2

    def sift_down(self, i, k = ''):
        ln = k + 1 if k != '' else len(self)
        while (2*i + 1 < ln and self.items[i] > self.items[2*i + 1]) or (2*i + 2 < ln and self.items[i] > self.items[2*i + 2]):
            if (2*i + 2 < ln and self.items[2*i + 2] > self.items[2*i + 1]):
                self.items[i], self.items[2*i + 1] = self.items[2*i + 1], self.items[i]
                i = 2*i + 1
            elif (2*i + 2 < ln):
                self.items[i], self.items[2*i + 2] = self.items[2*i + 2], self.items[i]
                i = 2*i + 2
            else:
                self.items[i], self.items[2*i + 1] = self.items[2*i + 1], self.items[i]
                i = 2*i + 1

    def update(self, i, x):
        self.items[i] = x
        self.sift_up(i)
        if self.items[i] == x: self.sift_down(i)
    
    def sort(self, rev = False):
        
        k = len(self) - 1
        while k != 0:
            self.items[0], self.items[k] = self.items[k], self.items[0]
            self.sift_down(0, k - 1)
            k -= 1
        if rev: return self.items
        else:
            self.items.reverse()
            return self.items