from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.garage = AVLTree()
        self.addedobject_bin = AVLTree()  # This is the another tree which will be sorted on basis of the object id and will have reference to the bin stored in the node
        self.bin_id = AVLTree()
    # public class

    def add_bin(self, bin_id, capacity): # checked no problem
        new_bin = Bin(bin_id,capacity)
        self.garage.add([capacity,bin_id],new_bin) 
        self.bin_id.add([bin_id,0],new_bin)
        


    def add_object(self, object_id, size, color): # problematic due to find_bin
        if self.garage.root is None: # baad me test case me error
            return None
        bin_to_fill = self.find_bin(self.garage.root,size,color)
        # try:print(bin_to_fill.value)
        # except:pass
        
        old_capacity = bin_to_fill.value.capacity
        # self.garage.print() 
        # print("---------------------------------------------")
        bin_to_fill.value.add_object(object_id,size,color)
        
        self.garage.add([bin_to_fill.value.capacity,bin_to_fill.value.bin_id],bin_to_fill.value)
        self.addedobject_bin.add([object_id,0],bin_to_fill.value)
        self.garage.remove([old_capacity,bin_to_fill.value.bin_id]) # garage AVL ko update ke liye
        # self.garage.print()
        # print("-------------------------------------------------")
        


            

    def delete_object(self, object_id): # add object ke vjh se problematic he
        try:    
            # Implement logic to remove an object from its bin
            bin_storing = self.addedobject_bin.find_node([object_id,0])
            self.garage.remove([bin_storing.value.capacity,bin_storing.value.bin_id]) # garage AVL ko update ke liye
            # self.garage.print()
            # print("------------------------------------------")
            bin_storing.value.remove_object(object_id) # in my function only key 0 is required so no tuple
            self.garage.add([bin_storing.value.capacity,bin_storing.value.bin_id],bin_storing.value)
            # self.garage.print()
            # print("-------------------------------------------")
            self.addedobject_bin.remove([object_id,0])
        except:
            raise NoBinFoundException

        

      



    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        bin_node = self.bin_id.find_node([bin_id,0])
        return (bin_node.value.capacity,bin_node.value.object_list())

        

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        try:
            object_node = self.addedobject_bin.find_node([object_id,0])
            return object_node.value.bin_id
        except:
            raise NoBinFoundException
        
    
    def find_bin(self,root,object_size,object_color): # isme problem he ye mera shi type ka node return krke nhi de rha
        
        # blue and yellow under compact fit algorithm
        # And if in me koi do bin same size ki ho then bin_id se dekhna he
        if object_color is Color.BLUE :  # Least ID
            if root is None : # case when root itself is none 
                raise NoBinFoundException
            current = root
            temp= root
            while current is not None:
                if current.key[0] >= object_size:
                    if current.key[0] < temp.key[0] or (current.key[0] == temp.key[0] and current.key[1]<temp.key[1]):
                        temp = current
                    if current.left is not None:
                        current = current.left
                    else : 
                        break
                else:
                    if current.right is not None:
                        current = current.right
                        if current.key[0] >= object_size:
                            temp = current
                    else:
                        break
            bin_node = temp

            if bin_node.key[0]<object_size:
                raise NoBinFoundException
            else:
                return bin_node
            
        
                
            
        elif object_color is Color.YELLOW : # Greatest ID
            if root is None :
                raise NoBinFoundException
            temp = root
            current = root
            while current is not None:
                if current.key[0] >object_size:
                    if current.key[0] < temp.key[0] or (current.key[0]) == temp.key[0] and current.key[1] >temp.key[1]:
                        temp = current
                    if current.left is not None:
                        current = current.left
                    
                    else:
                        break
                elif current.key[0] == object_size:
                    if current.key[0] < temp.key[0] or (current.key[0]) == temp.key[0] and current.key[1] >temp.key[1]:
                        temp = current
                    if current.right is not None:
                        current = current.right
                    else:
                        break
                else:
                    if current.right is not None:
                        current = current.right
                        if current.key[0]>=object_size:
                            temp = current
                    else:
                        break
            current = root
            while current is not None:
                if current.key[0]< temp.key[0]:
                    current = current.right
                elif current.key[0] > temp.key[0]:
                    current = current.left
                elif current.key[0] == temp.key[0] and current.key[1] > temp.key[1]:
                    temp =current
                    if current.right:
                        current = current.right
                    else:
                        break
                else :
                    break
            if temp is None:
                raise NoBinFoundException
            bin_node = temp
            if bin_node.key[0]< object_size:
                raise NoBinFoundException
            else :
                return bin_node
 

            
        # red and green under largest fit algorithm
        elif object_color is Color.RED : # Least ID
            if root is None :
                raise NoBinFoundException
            temp = root
            current = root
            max_node = self.garage.find_max()
            while current is not None:
                if current.key[0] < max_node.key[0]:
                    if current.right is not None :current  = current.right
                    else :
                        bin_node = temp
                        break
                else:
                    temp = current
                    if current.right is None:
                        bin_node = temp
                        break
                    else:
                        if current.left is not None:
                            current = current.left
                        else:
                            bin_node = temp
                            break
            if bin_node.key[0] < object_size:
                raise NoBinFoundException
            return bin_node
                            
                        
                        
                        


        elif object_color is Color.GREEN : # Greatest ID
            if root is None :
                raise NoBinFoundException
            else :
                maximum_node =  self.garage.find_max() 
                if maximum_node.key[0] < object_size :
                    raise NoBinFoundException
                else :
                    return maximum_node       # since the node with the greatest id will anyway be on right 


# gcms = GCMS()
# gcms.add_bin(1234, 10)
# gcms.add_bin(4321, 20)
# gcms.add_bin(1111, 15)
# gcms.add_bin(5555,20)
# gcms.add_object(369,10,Color.BLUE)
# #object_node = gcms.addedobject_bin.find_node([369,])
# gcms.garage.print()
# print(gcms.bin_info(1234))
# # gcms.delete_object(369)
# # print(gcms.bin_info(1234))
    
# gcms = GCMS()

# gcms.add_bin(1234, 10)
# gcms.add_bin(4321, 20)
# gcms.add_bin(1111, 15)
# gcms.add_bin(369,17)

# try:
#     gcms.add_object(8989, 6, Color.GREEN )
# except: 
#     print("Object 1 was not able to be added")

# try:
#     gcms.add_object(2892, 9, Color.GREEN )
# except: 
#     print("Object 2 was not able to be added")

# try:
#     gcms.add_object(4839, 8, Color.GREEN)
# except: 
#     print("Object 3 was not able to be added")
# gcms.add_object(3283, 2, Color.GREEN)
# try:
#     gcms.add_object(3283, 2, Color.GREEN)
# except: 
#     print("Object 4 was not able to be added")

# try:
#     gcms.add_object(8983, 8, Color.GREEN)
# except: 
#     print("Object 5 was not able to be added")

    

# gcms.garage.print()
# print(gcms.bin_info(1234))
# print(gcms.bin_info(4321))
# print(gcms.bin_info(1111))
# print(gcms.bin_info(369))
