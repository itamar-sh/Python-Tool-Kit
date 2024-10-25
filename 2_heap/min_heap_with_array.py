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

    def extract_min(self) -> None:
        # O(log(n))
        min_val = self.heap[0]
        if not self.heap:
            return ValueError("Heap is empty")
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.max_heapify(0)
        return min_val

    def getMin(self) -> int:
        # O(1)
        return self.heap[0] if self.heap else None

    def getParent(self, val_index) -> int:
        return (val_index - 1) // 2

    def get_childs(self, val_index):
        left_index = val_index * 2 + 1
        right_index = val_index * 2 + 2
        left_child = self.heap[left_index] if left_index <= len(self.heap) else None
        right_child = self.heap[right_index] if right_index <= len(self.heap) else None
        return left_index, left_child, right_index, right_child

    def max_heapify(self, index):
        """
        This helper method gets index of known smaller than his childs element in the heap and fix the heap.
        It is in use of this functions:
        1) build_min_heap.
        2) extract_min.
        The logic is to push down the element, since it's known the element is smaller than his parents.
        """
        if index >= len(self.heap):
            return

        left_index, left_child, right_index, right_child = self.get_childs(index)
        while index < len(self.heap) and self.heap[index] > min(left_child, right_child):
            if left_child <= right_child:
                self.heap[index], self.heap[left_index] = self.heap[left_index], self.heap[index]
                index = left_index
            else:
                self.heap[index], self.heap[right_index] = self.heap[right_index], self.heap[index]
                index = right_index
            left_index, left_child, right_index, right_child = self.get_childs(index)