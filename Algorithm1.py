import heapq

class Grid:
    def __init__(self,grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    #Determines which move is correct
    def movement_validation(self, r,c):
        #directions: [(up), (down), (left),(right)]
        movement_dir =[(-1,0),(1,0),(0,-1),(0,1)] 
        stored_values = []
        for dr, dc in movement_dir:
            new_r = r + dr
            new_c = c + dc
            
            #Check to stay inside grid
            if 0<= new_r < self.rows  and 0 <= new_c <self.cols:
                #Determine if movement is allowed 0 means yes
                if self.grid[new_r][new_c] == 0:
                    stored_values.append((new_r, new_c))
        return stored_values

    def djikstra_alg(self,start, target):
        heap =[]
        dist ={}

        heapq.heappush(heap, (0, start[0], start[1]))
        dist[start] = 0

        while heap:
            d,r,c = heapq.heappop(heap)

input1 = [
    [0,0,1,0,0,0],
    [1,0,1,0,1,0],
    [0,0,0,0,1,0],
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [1,1,0,0,0,0]
]
grid_input = Grid(input1)
start = (0,0)
target = (5,5)

input2 = [
    [0,0,0,1,0,0],
    [1,1,0,1,0,1],
    [0,0,0,1,0,0],
    [0,1,1,1,1,0],
    [0,0,0,1,0,0],
    [0,1,0,1,0,0]
]

grid_input2 = Grid(input2)
start = (0,0)
target =(5,5)
