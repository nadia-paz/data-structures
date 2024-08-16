"""
Heaps look like binary trees, but the root is eather max or min of all values.
Heaps are complete (fills from left to right with no gaps).
Heaps allow duplicates.

Heaps are stored as lists, not as trees. The 1st index of a  heap is 1 instead of 0.
Each parent has children located on the indecies:
2i and 2i+1, where i is parent's index
Each child has a parent on the index i // 2, where i is a child's index

We can either have None on the index 0 or re-write a bit aequations to adjust 
the root to be on the index 0
"""

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def _left_child(self, index):
        # returns an index of a left child 
        return 2 * index + 1
    
    def _righ_child(self, index):
        # returns an index of a right child 
        return 2 * index + 2
    
    def _parent(self, index):
        # returns a parent's index
        return (index - 1) // 2

    def _swap(self, index1, index2):
        # swaps values of 2 elements in the heap on the indeces
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def _sink_down(self, index):
        max_index = index
        
        while True:
            left_index = self._left_child(index)
            right_index = self._righ_child(index)

            if left_index < self.size and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            
            if right_index < self.size and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
    
    def insert(self, value):
        """
        Insert a value into a heap. The method first inserts the value in the end of the heap,
        then moves up untill it's on the correct place.
        """
        # current keeps an index of inserted value
        current = self.size 
        self.heap.append(value)
        self.size += 1

        # as long as:
        # - current index > 0, and
        # - the parent's value is smaller than the inserted value
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            # swap values on current and parent indecies
            self._swap(current, self._parent(current))
            # assign the current to the parent index
            current = self._parent(current)
    
    def remove(self):
        """
        Removes the root - the maximum value of the heap.
        The last value of the heap is placed on the top (to make the heap complete), 
        and then sinks down, until it's on the correct place
        """
        if self.size == 0:
            return None
        if self.size == 1:
            self.size = 0
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        # important! size -= 1 BEFORE sink_down
        self.size -= 1
        self._sink_down(0)

        return max_value


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

def stream_max(nums):
    # return the list of the same length as nums
    # where each element is the current max element in nums
    result = []
    heap = MaxHeap()
    
    for n in nums:
        heap.insert(n)
        result.append(heap.heap[0])
    
    return result

def heap_sort(nums:list, ascending = True):
    '''
    Heap sort algorithm
    '''
    length = len(nums)
    heap = MaxHeap()
    result = [None for x in range(length)]
    
    for n in nums:
        heap.insert(n)
    if ascending:
        for i in range(length):
            result[length - i - 1] = heap.remove()
            # print(result)
    else:
        for i in range(length):
            result[i] = heap.remove()
            # print(result)
    return result

nums = [67, 45, 34, 23, 1, 12, -9, 0]
h = MaxHeap()
for n in nums:
    h.insert(n)
show_tree(h.heap)
print(h.heap)
print("Ascending sort:", heap_sort(nums))
print("Descending sort:", heap_sort(nums, ascending=False))