# Max-Heap Implementation in Python

📄 [View PDF Explanation (Farsi)](Doc/Max-Heap.pdf)

This repository contains an implementation of the **Max-Heap** data structure in Python, based on the classic algorithms used for heap construction, insertion, deletion, and heap sort.

<img align= "center" src= "https://github.com/chevil-dev/MaxHeap/blob/main/images/00.png" width = "300" >

## 📚 Description

A **Max-Heap** is a complete binary tree where the value of each parent node is greater than or equal to the values of its children. This structure is useful for implementing priority queues and for efficient sorting (Heap Sort).

This project provides:

- Heap construction (`build_max_heap`)
- Insertion of new elements
- Increasing the value of an element
- Deletion of the maximum element
- Heap sort (descending order)

## 📌 Features

- `max_heapify`: Ensures the Max-Heap property is maintained at a given node.
- `build_max_heap`: Converts an unsorted list into a valid Max-Heap.
- `increase`: Increases the value of an element and restores the heap structure.
- `insert`: Inserts a new element into the heap.
- `delete_max`: Removes and returns the maximum value from the heap.
- `sort_heap`: Sorts the heap in descending order using heap sort.

## 🧠 Algorithms

The implementation is based on the following algorithms:

1. **Max-Heapify** — O(log n)
2. **Build-Max-Heap** — O(n)
3. **Increase** — O(log n)
4. **Insert** — O(log n)
5. **Delete-Max** — O(log n)
6. **Sort-Heap** — O(n log n)

## 🧾 Python Code
```python

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
        self.increase(len(self.heap) - 1, value)
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
```

[View python code](MaxHeap.py)
