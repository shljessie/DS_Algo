"""
Breadth First Search
1. start from one node
2. check all of its connections first
3. before moving on to the next node

Code Architecture 
1. visted = once visited put here, tracks order of search in BFS
2. queue = next node to check, put items in current node based on current node connections

create a queue Q 
mark v as visited and put v into Q 
while Q is non-empty 
    remove the head u of Q 
    mark and enqueue all (unvisited) neighbours of u

path finding algorithm 에 많이 쓰임
"""