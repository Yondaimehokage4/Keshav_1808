class Heap:
    
    def __init__(self, comparison_function, init_array):
        self.comparison_function = comparison_function
        self.heap_tree = init_array
        for i in range(len(self.heap_tree)//2 - 1, -1, -1):
            self._heapifydown(i)
          
    def insert(self, value):
        self.heap_tree.append(value)
        self._heapifyup(len(self.heap_tree) - 1)
        
    def extract(self):
        if len(self.heap_tree) == 0:
            raise Exception("Heap is empty")
        if len(self.heap_tree) == 1:
            return self.heap_tree.pop()
        self._swap(0, len(self.heap_tree) - 1)
        root = self.heap_tree.pop()
        self._heapifydown(0)
        return root
    
    def top(self):
        if len(self.heap_tree) == 0:
            raise Exception("Heap is empty")
        return self.heap_tree[0]
    
    def print(self):
        for i in range (0,len(self.heap_tree)):
            print(self.heap_tree[i],end=" ")
    
    def _parent(self, index):
        if self._has_parent(index):
            return (index - 1) // 2
        return None
        
    def _left(self, index):
        if self._has_left(index):
            return 2 * index + 1
        return None
    
    def _right(self, index):
        if self._has_right(index):
            return 2 * index + 2
        return None
    
    def _has_left(self, index):
        return 2 * index + 1 < len(self.heap_tree)
        
    def _has_right(self, index):
        return 2 * index + 2 < len(self.heap_tree)
    
    def _has_parent(self, index):
        return (index - 1) // 2 >= 0
    
    def _swap(self,index1,index2):
        if index1 > len(self.heap_tree) or index2 > len(self.heap_tree):
            raise Exception("Invalid Index")  
        else:
            temp = self.heap_tree[index1]
            self.heap_tree[index1] = self.heap_tree[index2]
            self.heap_tree[index2] = temp
        
        
    def _heapifyup(self,child):
        if child is None:
            child = len(self.heap_tree) - 1
        parent_index = self._parent(child)
        if parent_index is not None and self.comparison_function(self.heap_tree[child],self.heap_tree[parent_index]):
            self._swap(child,parent_index)
            return self._heapifyup(child = parent_index)
        else:
            return self.heap_tree
    
    def _heapifydown(self, index):
        if self._has_left(index):
            smaller_child_index = self._left(index)
            if self._has_right(index) and self.comparison_function(self.heap_tree[self._right(index)], self.heap_tree[smaller_child_index]):
                smaller_child_index = self._right(index)

            if not self.comparison_function(self.heap_tree[index], self.heap_tree[smaller_child_index]):
                self._swap(index, smaller_child_index)
                self._heapifydown(smaller_child_index)

        
    

























        
    
    



        
    
