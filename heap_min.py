class MinHeap:
    def __init__(self):
        self.heap = []

    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def _sink_down(self, index):
        min_index = 0 
        
        lindex = self._left_child(index)
        rindex = self._right_child(index)
        
        if lindex < len(self.heap) and self.heap[lindex] < self.heap[min_index]:
            min_index = lindex
        
        if rindex < len(self.heap) and self.heap[rindex] < self.heap[min_index]:
            min_index = rindex
            
        if index != min_index:
            self._swap(min_index, index)
            index = min_index
        else:
            return

    def insert(self, value):
        current = len(self.heap)
        self.heap.append(value)

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
            
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_value

import math
from io import StringIO

def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

h = MinHeap()
h.insert(5)
h.insert(9)
h.insert(4)
h.insert(1)
h.insert(20)
h.insert(5)
h.insert(13)
print(h.heap)
show_tree(h.heap)

removed = h.remove()
print(f'Removed: {removed}, Heap: {h.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = h.remove()
print(f'Removed: {removed}, Heap: {h.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = h.remove()
print(f'Removed: {removed}, Heap: {h.heap}')  # Removed: 6, Heap: [8, 12, 10]