from node import Node

#def comp_1(node_1, node_2):
  #  pass

class AVLTree:
    def __init__(self): #compare_function=comp_1):
        self.root = None
        self.size = 0
    #    self.comparator = compare_function # is function ki koi jaruat he nhi hme vese
    
        
    # mota mota ye kr rhe :(public class)
    def add(self,key,value):
        self.root = self._insert(self.root,key,value)
    
    def remove(self,key):
        self.root = self._delete(self.root,key)

    def print(self):
        return self._inorder_traversal(self.root)   

    def find_max(self):
        return self._find_max(self.root)
    
    def find_min(self):
        return self._find_min(self.root)
    
    def find_node(self,key):
        return self._findnode(self.root,key)
  
                
    # jo bhi andr kchra chlega (private method):

    def _height(self, Node):
        if Node is None:
            return 0
        return Node.height
    # everytime in definitions below I will update height of the node so the height of the node is defined by the _update_height function
    def _update_height(self, Node):
        Node.height = 1 + max(self._height(Node.left), self._height(Node.right))

    def _balance_factor(self, Node):
        return self._height(Node.left) - self._height(Node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self._update_height(y)
        self._update_height(x)

        # Return the new root
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self._update_height(x)
        self._update_height(y)

        # Return the new root
        return y

    def _balance(self, node):
        if node is None:
            return None
        
        self._update_height(node)
        balance = self._balance_factor(node)

        # Left Left Case
        if balance > 1 and node.left.key[0]-node.key[0] < 0:
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and node.right.key[0]-node.key[0] > 0:
            return self._rotate_left(node)

        # Left Right Case
        if balance > 1 and node.left.key[0]-node.key[0] > 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Left Case
        if balance < -1 and node.right.key[0]- node.key[0] < 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert(self, node, key, value):
        if node is None:
            self.size+=1
            return Node(key,value)

        if key[0] - node.key[0] < 0:
                node.left = self._insert(node.left, key, value)
        elif key[0] - node.key[0] >0 :
                node.right = self._insert(node.right, key, value)
        elif key[0] - node.key[0] == 0:
            if node.key[1] != 0 :
                if key[1] < node.key[1]:
                    node.left = self._insert(node.left,key,value)
                elif key[1] > node.key[1]:
                    node.right = self._insert(node.right,key,value)
            else :
                return # check
        self._update_height(node)
        return self._balance(node) # this is a recursive pattern which recurselveily balances tree to the root

    def _findnode(self,node,key):
        if node is None:
            return None
        else :
            if node.key[0] < key[0] and node.right is not None:
                return self._findnode(node.right,key)
            elif node.key[0] > key[0] and node.left is not None:
                return self._findnode(node.left,key)
            elif  node.key[0] == key[0] :
                if key[1] == 0:
                    return node
                else :
                    if key[1] < node.key[1] :
                        return self._findnode(node.left,key)
                    elif key[1] > node.key[1]:
                        return self._findnode(node.right,key)
                    elif key[1] == node.key[1]:
                        return node
        return None

        
    
    # def _findbin_samekey(self,key,bin_id): # This method is case of multople bins of same capacity. 
    #     node = self.find_node(key,bin_id)
    #     if node is None:
    #         return
    #     bin_node = node.AVLTree.find_node(bin_id,key)
    #     return bin_node

    def _find_min(self, node):
        if node is None or node.left is None:
            return node
        return self._find_min(node.left)

    def _find_max(self,node):
        if node is None or node.right is None:
            return node
        return self._find_max(node.right)


    def _delete(self, node, key):
        if node is None:
            return node

        # Perform standard BST delete
        if key[0]-node.key[0] < 0:
            node.left = self._delete(node.left, key)
        elif key[0]-node.key[0]> 0:
            node.right = self._delete(node.right, key)
        # case deletion of bin having same capacity as some other bin
        elif node.left and node.key[0] == node.left.key[0] and key[1]<node.key[1]:
                node.left = self._delete(node.left,key)

        elif node.right and node.key[0] == node.right.key[0] and key[1]>node.key[1]:
                node.right = self._delete(node.right,key)
        else:
            if node.key != key : # case required node doesn't exist in tree
                return 

            # Node with only one child or no child
            if node.left is None:
                self.size -= 1
                return node.right
            elif node.right is None:
                self.size -= 1
                return node.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._find_min(node.right)

            # Copy the inorder successor's content to this node
            node.key = temp.key
            node.value = temp.value

            # Delete the inorder successor
            node.right = self._delete(node.right, temp.key)

        # If the tree had only one node then return
        if node is None:
            return node

        # Update height of the current node
        self._update_height(node)

        # Balance the node
        return self._balance(node)

    def _inorder_traversal(self, node):
        if node:
            if node.left:
                self._inorder_traversal(node.left)
            print(f"Key: {node.key}")
            if node.right:
                self._inorder_traversal(node.right)
            
# AVL tree is success HURRAY!!!!
# check = AVLTree()
# check.add([20,369],1)
# check.add([30,69],2)
# check.add([50,450],3)
# check.add([80,7638],4)
# check.add([10,243],5)
# check.add([15,325],6)
# check.add([15,54],7)
# check.add([15,45],8)
# check.remove([15,54])
# check.remove([10,243])
# check.print() 
# node = check.find_node([15,45])
# print(node.value)
# print(check.find_max().key)
# print(check.find_min().key)

