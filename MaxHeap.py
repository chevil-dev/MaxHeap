class MaxHeap:
    def __init__(self):
        self.heap = []
    def max_heapify(self , i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        if left < len(self.heap):
            if self.heap[left] > self.heap[i]:
                largest = left
            else:
                largest = i
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    def build_max_heap(self , array):
        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.max_heapify(i)
    def increase(self , i, value):
        if value < self.heap[i]:
            raise ValueError ("New value is smaller than current value")
        self.heap[i] = value
        while i > 0 and self.heap[i] > self.heap[(i-1) // 2]:
            self.heap[i], self.heap[(i-1) // 2] = self.heap[(i-1) // 2], self.heap[i]
            i = (i-1) // 2
    def insert(self , value):
        self.heap.append(float('-inf'))
        self.increase(self , len(self.heap) - 1, value)
    def delete_max(self):
        if len(self.heap) < 1:
            raise IndexError ("Heap is empty.")
        maxValue = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.max_heapify(0)
        return maxValue
    def sort_heap(self):
        sortHeap = []
        while len(self.heap) > 0:
            sortHeap.append(self.delete_max ())
        return sortHeap[::-1]
