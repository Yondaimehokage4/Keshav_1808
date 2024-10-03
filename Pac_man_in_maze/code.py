#main 
from maze import *
from navigator import *

def is_valid(x : int, y : int, rows : int, cols : int) -> bool:
    if(x < 0 or x >= rows):
        print("The row of cell", (x, y), "is out of bounds, hence this path is invalid.")
        return False
    elif(y < 0 or y >=cols):
        print("The column of cell", (x, y), "is out of bounds, hence this path is invalid.")
        return False
    return True
def is_neighbour(x1 : int, y1 : int, x2 : int, y2 : int) -> bool:
    return abs(x2-x1) + abs(y2-y1) == 1
if __name__ == "__main__":
    
    ## YOU CAN TWEAK THESE PARAMETERS IN ORDER TO GENERATE MORE TESTCASES
    grid_rows = 4
    grid_cols = 4
    ghosts = [(0, 1), (2, 2), (3, 1)]
    start_point = (2, 0)
    end_point = (2, 3)
    ## This is where the checker logic starts
    sample_grid = Maze(grid_rows, grid_cols)
    for ghost in ghosts:
        sample_grid.add_ghost(ghost[0], ghost[1])
        if(not sample_grid.is_ghost(ghost[0], ghost[1])):
            print("The cell", ghost, "is supposed to contain a ghost, but your program says otherwise!\nTESTCASE FAILED")
            exit(1)
    sample_grid.print_grid()
    '''
    EXPECTED OUTPUT : 
    0 1 0 0
    0 0 0 0
    0 0 1 0
    0 1 0 0
    '''
    PacManInstance = PacMan(sample_grid) 
    try:
        path = PacManInstance.find_path(start_point, end_point) 
        isPathValid = True
        if(path[0] != start_point):
            print("The path is supposed to begin with the tuple", start_point, ", hence this path is invalid.")
            isPathValid = False
        if(path[-1] != end_point):
            print("The path is supposed to end with the tuple", end_point, ", hence this path is invalid.")
            isPathValid = False
        allCells = set()
        for cell in path:
            if(is_valid(cell[0], cell[1], grid_rows, grid_cols) and sample_grid.grid_representation[cell[0]][cell[1]] == 1):
                print("The cell", cell, "that you have in your path is not vacant, hence this path is invalid.")
                isPathValid = False
            if(cell in allCells):
                print("The cell", cell, "that you have in your path is a duplicate cell, hence this path is invalid.")
                isPathValid = False
            allCells.add(cell)
        for i in range(len(path) - 1):
            if(not is_neighbour(path[i][0], path[i][1], path[i+1][0], path[i+1][1])):
                print("Cells", path[i], "and", path[i+1], "are not neighbours, hence this path is invalid.")
                isPathValid = False
        if(isPathValid):
            print("PATH FOUND SUCCESSFULLY!")
        else:
            print("TESTCASE FAILED")
    except (PathNotFoundException):
        print("TESTCASE FAILED. A VALID PATH DOES EXIST BETWEEN THESE TWO LOCATIONS")





# Navigator:

from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        
        (x1,y1) = start
        if self.navigator_maze[x1][y1] == 1:
            raise PathNotFoundException
        (x2,y2) = end
        work = Stack()
       
        visited = []
        work.push((start,[(start)]))
        while not work.is_empty():
            (x,y),path = work.pop()
            
            if (x,y) == None:
                break
            
            if (x,y) not in visited:
                visited.append((x,y))
                
            
            if (x,y) == (x2,y2):
                return path
            
            if y>0 and  y<=len(self.navigator_maze[0])-1 and (work.leftx(x,y),work.lefty(x,y)) not in visited and self.navigator_maze[work.leftx(x,y)][work.lefty(x,y)] !=1:
              work.push(((work.leftx(x,y),work.lefty(x,y)),path+[(work.leftx(x,y),work.lefty(x,y))]))
            
            if y<len(self.navigator_maze[0])-1 and y>=0 and (work.rightx(x,y),work.righty(x,y)) not in visited and self.navigator_maze[work.rightx(x,y)][work.righty(x,y)] !=1:
                work.push(((work.rightx(x,y),work.righty(x,y)),path+[(work.rightx(x,y),work.righty(x,y))]))
                
            if x<=len(self.navigator_maze)-1  and x>0 and (work.topx(x,y),work.topy(x,y)) not in visited and  self.navigator_maze[work.topx(x,y)][work.topy(x,y)] !=1:
                work.push(((work.topx(x,y),work.topy(x,y)),path+[(work.topx(x,y),work.topy(x,y))]))
                
            if x>=0 and x<len(self.navigator_maze)-1 and (work.bottomx(x,y),work.bottomy(x,y))  not in visited and self.navigator_maze[work.bottomx(x,y)][work.bottomy(x,y)] !=1:
                work.push(((work.bottomx(x,y),work.bottomy(x,y)),path+[(work.bottomx(x,y),work.bottomy(x,y))]))
        # koi to sorting mechanism krna pdega, jo element ke baad uske neighbours hi daale bs  
        
            
        raise PathNotFoundException


# exception:
class PathNotFoundException(Exception):
    ## DO NOT MODIFY ANYTHING IN THIS CLASS
    def __init__(self):
        super().__init__("A path does not exist between the specified start and end points")



# maze:
class Maze:
    def __init__(self, m: int, n : int) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        ## We initialise the list with all 0s, as initially all cells are vacant
        self.grid_representation = []
        for row in range(m):
            grid_row = []
            for column in range(n):
                grid_row.append(0)
            self.grid_representation.append(grid_row)
    
    def add_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
       self.grid_representation[x][y]=1
            
    def remove_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        self.grid_representation[x][y]=0
            
    def is_ghost(self, x : int, y: int) -> bool:
        # IMPLEMENT YOUR FUNCTION HERE
         return self.grid_representation[x][y]
       
    def print_grid(self) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        for row in self.grid_representation:
            for col in row:
                print(col,end=" ")
            print("\n")
        

# Stack :
class Stack():
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        # From a stack having left right top bottom then while moving across 
        # the grid pop the elements through which you have already passed
        self.list_Stack=[]
    
    def push(self,x):
        self.list_Stack.append(x)
    def is_empty(self):
        if(len(self.list_Stack)==0):
            return True
        else :
            return False
    def pop(self):
        if len(self.list_Stack) != 0:
            x= self.top()
            self.list_Stack.pop()
            return x
        else :
            raise Exception('Stack is empty')
    def len(self):
        return len(self.list_Stack)
    def top(self):
        if(len(self.list_Stack)==0):
            raise Exception('the list is empty')
        else :
            return self.list_Stack[-1]# used for last element
    
    def topx(self,x:int,y:int):
        return x-1
    def topy(self,x:int,y:int):
        return y
    def bottomx(self,x:int,y:int):
        return x+1
    def bottomy(self,x:int,y:int):
        return y
    def leftx(self,x:int,y:int):
        return x
    def lefty(self,x:int,y:int):
        return y-1
    def rightx(self,x:int,y:int):
        return x
    def righty(self,x:int,y:int):
        return y+1
    def stack(self,x:int,y:int):
        self.push((self.topx(x, y), self.topy(x, y)))
        self.push((self.bottomx(x, y), self.bottomy(x, y)))
        self.push((self.rightx(x, y), self.righty(x, y)))
        self.push((self.leftx(x, y), self.lefty(x, y)))

    
    
  
