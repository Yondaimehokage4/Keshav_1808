from avl import AVLTree
from object import Object
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.container = AVLTree()
        self.list = []

    def add_object(self, object_id,size,color):
        # Implement logic to add (an object to this bin)
        # Since we need to find object at the time of deletion in logn time our bin will also be an AVL tree 
        if size > self.capacity:
            return 
        else :
            self.container.add([object_id,size],Object(object_id,size,color))
            self.capacity -= size


    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        # Since the deletion is required in logn + logm time this data structure is implemented 
        key0 = object_id
        object_node = self.find_objectnode(self.container.root,key0)
        self.container.remove([object_id,object_node.key[1]])

        self.capacity += object_node.value.size
        
    
    def find_objectnode(self,root,key0): # Finiding object node from the given object_id 
        if root is None :
            return None
        else :
            if key0 - root.key[0] < 0 :
                return self.find_objectnode(root.left,key0)     
            elif key0 - root.key[0] > 0 :
                return self.find_objectnode(root.right,key0)   
            return root
        return None
    

    def object_list(self):
        self.list = []
        self._inorder_traversal(self.container.root)
        return self.list


    def _inorder_traversal(self, node):
        if node:
            if node.left:
                self._inorder_traversal(node.left)
            if node.key[0]:
                self.list.append(node.key[0])
            if node.right:
                self._inorder_traversal(node.right)
        else:
            return




#bin is workking too yahooooo!!!!
# new_bin = Bin(369,15)
# new_bin.add_object(123,5,1)
# new_bin.add_object(124,5,1)
# new_bin.add_object(125,5,1)
# new_bin.remove_object(124)
# new_bin
# print(new_bin.capacity)
# print(new_bin.object_list())



