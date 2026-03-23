# CPSC-335-10_Project-2
- Richard Le
- Richard.le@csu.fullerton.edu
- Marco Chavez
- marco_chavez@csu.fullerton.edu
- Arman Madatyan 
- armanmadatyan@csu.fullerton.edu
- Jeremy Mejia
- fr.jeremy@csu.fullerton.edu

# CPSC 335 — Project 2 — Algorithm 1
## Shortest Escape Path in a Maze

## Description
This program finds the minimum number of moves required to travel
from a starting cell to a target cell in a rectangular maze.

The maze is represented as a 2D grid:
- 0 = open cell
- 1 = blocked cell

The program allows movement only in four directions:
- up
- down
- left
- right

The algorithm uses Dijkstra’s algorithm with a priority queue
to compute the shortest path.
If the target cannot be reached, the program returns -1.

## Sample Outputs
Example 1 Output: 10
Example 2 Output: -1

## How to Run
Make sure Python 3 is installed.

Run:
python algo1.py


# CPSC 335 — Project 2 — Algorithm 2
## Boats to Save People

## Description
This program computes the minimum number of boats needed to rescue
all people without exceeding the boat weight limit.

Rules:
- Each boat can carry at most two people
- The total weight in a boat cannot exceed the given limit
- Every person must be placed in exactly one boat

The algorithm sorts the list of weights and uses a greedy
two-pointer strategy:
- pair the lightest and heaviest person if possible
- otherwise send the heaviest person alone

This guarantees the minimum number of boats.

## Sample Outputs
Example 1 Output: 3
Example 2 Output: 5

## How to Run
Make sure Python 3 is installed.

Run:
python algo2.py