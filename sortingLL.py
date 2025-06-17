import time

class Node:
    def __init__(self, v, n=None): self.v, self.n = v, n

class LinkedList:
    def __init__(self): self.h = None
    def insert_sorted(self, v):
        if not self.h or self.h.v >= v: self.h = Node(v, self.h); return
        c = self.h
        while c.n and c.n.v < v: c = c.n
        c.n = Node(v, c.n)
    def to_list(self):
        r, c = [], self.h
        while c: r.append(c.v); c = c.n
        return r

def counting_sort_with_linked_list(arr):
    count = [0] * (max(arr) + 1)
    for num in arr: count[num] += 1
    ll = LinkedList()
    for i, cnt in enumerate(count):
        for _ in range(cnt): ll.insert_sorted(i)
    return ll.to_list()



n = int(input("eneter how many elements: "))
arr  = []
for i in range(0,n):
	arr.append(int(input()))
start = time.time()
print("Sorted array is:", counting_sort_with_linked_list(arr))
print("Time: %.6f seconds" % (time.time() - start))
