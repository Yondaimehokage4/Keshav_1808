import heap
import treasure  
from treasure import Treasure
# from custom import crewmate_Heap
from crewmate import CrewMate
from heap import Heap


class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        # Write your code here
        self.crewmate_having_treasure = [] # array that will have list of treasures
        self.crewmate_array =[]
        self.crewmate_comparision = lambda a,b : a.load<b.load
        for i in range(0,m):
            self.crewmate_array.append(CrewMate())
        self.crewmate_Heap = Heap(self.crewmate_comparision ,self.crewmate_array) # each element of crewmate_array is an class of CrewMate which contains current load of crewmate, we will use this  load to sort the Tree
                                                                                      
        
        
        
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        # Write your code here
        self.crewmate_Heap.heap_tree[0]._add_treasure(treasure) # sbse nlle insaan ko kaam dediya
        employed_worker  = self.crewmate_Heap.extract()
                # cooking....
        if treasure.arrival_time - employed_worker.load >=0:
            employed_worker.load = treasure.size +  treasure.arrival_time # implementing relative load  , time = O(1)
        else:
            employed_worker.load = employed_worker.load - treasure.arrival_time + treasure.size
                #cooked
        treasure.load_at_arrival = employed_worker.load
        print(f"|||{employed_worker.load} , {treasure.load_at_arrival}")
        self.crewmate_Heap.insert(employed_worker)# $
        print("--------------------")
        for i in range (0,len(self.crewmate_Heap.heap_tree)):
            print(self.crewmate_Heap.heap_tree[i].load,end=" ")
        # employed once hence add in the list
        if employed_worker.atleast_once_employed == 0:
            self.crewmate_having_treasure.append(employed_worker)   #O(1)
            employed_worker.atleast_once_employed =1



        
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
           List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
       
        # Write your code here
        treasury_list = []
        for i in range(0,len(self.crewmate_having_treasure)):
                print(f"employed_worker load: {self.crewmate_having_treasure[i].load}")
                treasury_list += self.crewmate_having_treasure[i].treasury
        return treasury_list



black_pearl = StrawHatTreasury(3)
Treasure1 = Treasure(1,8,1)
Treasure2 = Treasure(2,7,2)
Treasure3 = Treasure(3,4,4)
Treasure4 = Treasure(4,1,5)


black_pearl.add_treasure(Treasure1)
black_pearl.add_treasure(Treasure2)
black_pearl.add_treasure(Treasure3)
black_pearl.add_treasure(Treasure4)



print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

treasure_info_list = black_pearl.get_completion_time()
for i in range(0,len(treasure_info_list)):
    print(treasure_info_list[i].id)
print()
for j in range(0,len(black_pearl.crewmate_Heap.heap_tree)):
    black_pearl.crewmate_Heap.heap_tree[j]._get_completion_time()

for j in range(0,len(black_pearl.crewmate_Heap.heap_tree)):
    print(f"Crewmate {j} :")
    for i in range(0,len(black_pearl.crewmate_Heap.heap_tree[j].treasury)):
        print(f"id:{black_pearl.crewmate_Heap.heap_tree[j].treasury[i].id} ,priority:{black_pearl.crewmate_Heap.heap_tree[j].treasury[i].priority} ,loadatarrival: {black_pearl.crewmate_Heap.heap_tree[j].treasury[i].load_at_arrival}  ,completion_time:{black_pearl.crewmate_Heap.heap_tree[j].treasury[i].completion_time}")
        print(f"arrival time :{black_pearl.crewmate_Heap.heap_tree[j].treasury[i].arrival_time}")
    
    print()


        
    
    # You can add more methods if required