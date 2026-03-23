#Richard Le
#Richard.le@csu.fullerton.edu
#Marco Chavez
#marco_chavez@csu.fullerton.edu
#Arman Madatyan 
#armanmadatyan@csu.fullerton.edu
#Jeremy Mejia
#fr.jeremy@csu.fullerton.edu

import heapq

class Grid:
    def __init__(self,grid): 
        self.grid = grid            #creates 2D Grid
        self.rows = len(grid)       #num of rows
        self.cols = len(grid[0])    #num of cols

    #Determines which move is correct
    def movement_validation(self, r,c):
        """
        Returns all valid neighboring cells that can be moved to
        from position (r, c).
        A valid move:
        - stays inside the grid
        - lands on an open cell (value 0)
        """
        #directions: [(left),(up),(down),(right)]
        movement_dir =[(-1,0),(1,0),(0,-1),(0,1)] 
        stored_values = []
        # Check each direction
        for dr, dc in movement_dir:
            #calculates position
            new_r = r + dr
            new_c = c + dc
            
            #Check to stay inside grid
            if 0<= new_r < self.rows  and 0 <= new_c <self.cols:
                #Determine if movement is allowed 0 means yes
                if self.grid[new_r][new_c] == 0:
                    stored_values.append((new_r, new_c))

        return stored_values

    def djikstra_alg(self,start, target):
        # Min-heap priority queue:
        # stores tuples in the form (distance, row, col)
        heap =[]
        dist ={}  # dist dictionary stores the shortest known distance

        #starting position with a distance of 0
        heapq.heappush(heap, (0, start[0], start[1]))
        dist[start] = 0

        # Process cells until there are none left
        while heap:
            #d = current distance
            # r, c represents current position
            d,r,c = heapq.heappop(heap)

            #target reached
            if (r,c) == target:
                    return d
            
            #grid traversal using validation to determine correct path
            for i in self.movement_validation(r,c):
                new_r, new_c = i
                distance = d+1

                if (new_r, new_c) not in dist or distance < dist[(new_r, new_c)]: #Determine if new node is seen or shorter path found
                    dist[(new_r, new_c)] = distance #current best path
                    heapq.heappush(heap, (distance, new_r, new_c))
        
        #heap empty
        return-1        

start = (0,0)
target = (5,5)

# Example 1 from the project sheet
input1 = [
    [0,0,1,0,0,0],
    [1,0,1,0,1,0],
    [0,0,0,0,1,0],
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [1,1,0,0,0,0]
]
grid_input = Grid(input1)

# Example 2 from the project sheet
input2 = [
    [0,0,0,1,0,0],
    [1,1,0,1,0,1],
    [0,0,0,1,0,0],
    [0,1,1,1,1,0],
    [0,0,0,1,0,0],
    [0,1,0,1,0,0]
]

grid_input2 = Grid(input2)

# Print the result for both required test cases
print(grid_input.djikstra_alg(start, target))
print(grid_input2.djikstra_alg(start,target))