class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        # O(log(n))
        self.heap.append(val)
        val_index = len(self.heap)-1
        parent_index = self.getParent(val_index)
        while self.heap[parent_index] > val:
            self.heap[-1], self.heap[parent_index] = self.heap[parent_index], val
            parent_index = self.getParent(parent_index)

    def pop(self) -> None:
        # O(log(n))
        min_val = self.heap[0]
        if not self.heap:
            return ValueError("Heap is empty")
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if not self.heap:
            return min_val
        val_index = 0
        left_child = self.heap[1] if len(self.heap) > 1 else float('inf')
        right_child = self.heap[2] if len(self.heap) > 2 else float('inf')
        while self.heap[val_index] > min(left_child, right_child):
            if left_child <= right_child:
                self.heap[val_index], self.heap[left_index] = self.heap[left_index], self.heap[val_index]
                val_index = left_index
            else:
                self.heap[val_index], self.heap[right_index] = self.heap[right_index], self.heap[val_index]
                val_index = right_index
            left_index, left_child, right_index, right_child = self.getChilds(val_index)
        return min_val

    def getMin(self) -> int:
        # O(1)
        return self.heap[0] if self.heap else None

    def getParent(self, val_index) -> int:
        return (val_index - 1) // 2

    def getChilds(self, val_index):
        left_index = val_index * 2 + 1
        right_index = val_index * 2 + 2
        left_child = self.heap[left_child]
        right_child = self.heap[right_child]
        return left_index, left_child, right_index, right_child