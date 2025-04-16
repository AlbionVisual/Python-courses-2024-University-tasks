from sys import argv as entries
from simplequeue import Queue

nums = entries[1].split()
p1 = Queue()
p2 = Queue()

for i in nums[:len(nums) // 2]:
    p1.enqueue(i)
for i in nums[len(nums) // 2:]:
    p2.enqueue(i)

err = False

while (not p1.is_empty() and not p2.is_empty()) and not err:
    print("p1: " + " ".join(list(p1.items)), "p2: " + " ".join(list(p2.items)), sep='\n', end='\n\n')
    
    a1, a2 = [p1.dequeue()], [p2.dequeue()]
    while a1[-1] == a2[-1]: 
        a1 += [p1.dequeue()]; a2 += [p2.dequeue()] 
        if not a1[-1].isdigit() and not a2[-1].isdigit():
            print("Decks are equal: ")
            err = "Equal desks!"
            break
    
    if a1[-1] > a2[-1]: 
        a1 = [i for i in a1 if i.isdigit()]
        a2 = [i for i in a2 if i.isdigit()]
        for i in range(max(len(a1), len(a2))):
            if i < len(a1): p1.enqueue(a1[i])
            if i < len(a2): p1.enqueue(a2[i])
    else:
        a1 = [i for i in a1 if i.isdigit()]
        a2 = [i for i in a2 if i.isdigit()]
        for i in range(max(len(a1), len(a2))):
            if i < len(a2): p2.enqueue(a2[i])
            if i < len(a1): p2.enqueue(a1[i])

print("p1: " + " ".join(list(p1.items)), "p2: " + " ".join(list(p2.items)), sep='\n', end='\n\n')
