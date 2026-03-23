
# CPSC 335 - Project 2
# Problem 1: Shortest Escape Path in a Maze
# Name: Arman Madatyan

from collections import deque


def shortest_escape_path(grid, start, target):
    # Get grid dimensions
    rows = len(grid)
    cols = len(grid[0])

    # Unpack start and target positions
    sx, sy = start
    tx, ty = target

    # Check if start is outside the grid
    if sx < 0 or sx >= rows or sy < 0 or sy >= cols:
        return -1

    # Check if target is outside the grid
    if tx < 0 or tx >= rows or ty < 0 or ty >= cols:
        return -1

    # Check if start or target is blocked
    if grid[sx][sy] == 1 or grid[tx][ty] == 1:
        return -1

    # Keep track of visited cells so we don’t revisit them
    visited = [[False] * cols for _ in range(rows)]

    # Queue for BFS (stores row, column, and number of moves)
    q = deque()
    q.append((sx, sy, 0))

    # Mark starting cell as visited
    visited[sx][sy] = True

    # Possible movements: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Perform BFS
    while q:
        x, y, moves = q.popleft()

        # If we reach the target, return the number of moves
        if (x, y) == (tx, ty):
            return moves

        # Check all 4 directions
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # Check if next position is inside grid and valid
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True  # mark as visited
                    q.append((nx, ny, moves + 1))  # add to queue with +1 move

    # If target cannot be reached
    return -1


def main():
    # Simple test case
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]

    start = (0, 0)
    target = (2, 2)

    # Print result
    print(shortest_escape_path(grid, start, target))


if __name__ == "__main__":
    main()
