#Pseudocode for Shortest Escape 
Algorithm ShortestEscape (grid, sx, sy, tx, ty) 
Input:
    grid = 2D array of 0s and 1s
    (sx, sy) = starting cell
    (tx, ty) = target cell

Output:
    Minimum number of moves from start to target
    Return -1 if target cannot be reached

1. Let rows = number of rows in grid
2. Let cols = number of columns in grid
3. If start is outside the grid or target is outside the grid:
       return -1

4. If grid[sx][sy] = 1 or grid[tx][ty] = 1:
       return -1
5. Create a queue Q
6. Create a 2D visited array of size rows x cols, initialized to false
7. Enqueue (sx, sy, 0) into Q
   // 0 is the number of moves so far
8. Mark visited[sx][sy] = true

9. While Q is not empty:
       Dequeue (x, y, dist)

       If (x, y) = (tx, ty):
           return dist

       For each direction in {up, down, left, right}:
           nx = x + dx
           ny = y + dy

           If nx and ny are inside the grid
              AND grid[nx][ny] = 0
              AND visited[nx][ny] = false:

                 Mark visited[nx][ny] = true
                 Enqueue (nx, ny, dist + 1)

10. Return -1
