from heap import Heap
from treasure import Treasure
def comparision_treasure(a,b):
    if a.priority != b.priority:
        return a.priority < b.priority
    else:
        return a.id < b.id


class CrewMate:
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.treasury = []
        self.load = 0
        self.actual_load =0
        self.atleast_once_employed = 0
        self.treasure_heap = Heap(comparision_treasure,[])
    
    # Add more methods if required
    def completion_time_treasury(self):
        self._get_completion_time 
        return self.treasury



    # Private Methods:
    def _add_treasure(self,value):
        value.init2()
        self.treasury.append(value)

    def remove_last_added_treasure(self):
        self.treasury.pop()

    def _get_completion_time(self):
        if len(self.treasury)==1:
            self.treasury[0].completion_time = self.treasury[0].size+ self.treasury[0].arrival_time
        elif len(self.treasury)>=2:
            self.treasury[0].remaining_capacity = self.treasury[0].size
            self.treasury[0].priority = self.treasury[0].remaining_capacity + self.treasury[0].arrival_time
            self.treasure_heap.insert(self.treasury[0])
            backlog = self.treasury[0].arrival_time
            for i in range(1,len(self.treasury)):
                while (len(self.treasure_heap.heap_tree)>0) and (self.treasure_heap.heap_tree[0].remaining_capacity <= self.treasury[i].arrival_time - backlog):
                    processed_treasure = self.treasure_heap.extract()
                    processed_treasure.completion_time = processed_treasure.remaining_capacity+backlog
                    backlog = processed_treasure.completion_time
                
                if (len(self.treasure_heap.heap_tree)>0):
                    self.treasure_heap.heap_tree[0].remaining_capacity -= self.treasury[i].arrival_time - backlog
                    self.treasure_heap.heap_tree[0].priority = self.treasure_heap.heap_tree[0].remaining_capacity + self.treasure_heap.heap_tree[0].arrival_time
                backlog  = self.treasury[i].arrival_time

                self.treasury[i].remaining_capacity = self.treasury[i].size
                self.treasury[i].priority = self.treasury[i].remaining_capacity + self.treasury[i].arrival_time
                self.treasure_heap.insert(self.treasury[i])
           
            for j in range(0,len(self.treasure_heap.heap_tree)):
                element = self.treasure_heap.extract()
                element.completion_time = element.remaining_capacity + backlog
                backlog = element.completion_time 
            
    def print_HeapTreasure(self):
        self.treasure_heap.print()

    

    
