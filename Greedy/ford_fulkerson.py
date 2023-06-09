"""
2023.05.03 --> study some example coding questions 

Ford Fulkerson
** use when you need to find the max flow

<Use Case Example> 
Assuming steady conditions (Number of trains on a railway track at any instance of time must not exceeds the track's capacity), if we need to find what is the maximum number of trains (maximum flow) that we can send from City 
A to city B then the problem is known as the "Maximum Flow Problem" 

Greedy Algorithm within a Flow network
A term, flow network, is used to describe
a network of vertices and edges with a source (S) and a sink (T). 
Each vertex, except S and T, can receive and send an equal amount of stuff through it. 
S can only send and T can only receive stuff.
https://www.programiz.com/dsa/ford-fulkerson-algorithm 

Each path has a capacity like the amount of energy left after we go through the path
When choosing a path, we minus each of the path capacity by the minimum capacity in the path


** DFS vs BFS : https://www.freelancinggig.com/blog/2019/02/06/what-is-the-difference-between-bfs-and-dfs-algorithms/

** Stack vs Queue : Stack LIFO, Queue FIFO

graph = np.array([[0, 1, 1, 0],
                  [1, 0, 0, 1],
                  [1, 0, 0, 1],
                  [0, 1, 1, 0]])

the numbers represent the strength of the edges
graph = np.array([
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
])

2D representation of graphs to a node graph. 1 for the parts where there is an edge.
"""

"""
2023.05.04 Overall Review

< Ford Fulkerson Algorithm >

* Goal 
Find the Max Flow value in the graph. 
The max flow refers to the sum of the min capacities in the available paths in the graph.
<available paths> we have to subtract the capacities as we minus the graphs

* Code Architecture

[ Large Two parts ]
1. BFS Tree : keep track of visited paths and capacity availability
2. Ford Fulkerson : to find min capacities , sum capacities to find max flow

[ Things to note ]
1.2D matrix representation of graphs = weights
the row columns are the node values

graph = np.array([
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
])



Part 1. BFS Tree
We do BFS because we have to find all connected paths
BFS looks at all connected paths before it starts traversing

weights (graphs) , s (source,  number int value index) , t (sink) , parent (node above, no parent -1)

* visted list = initially False len of weights(graphs)
* queue = keep track of the node paths that are currently available

    visited = [False] * len(graph)
    queue =[] 

    queue[0] = s
    visited[s] = True

* start a while loop to while there is a node to check for path
    while queue:
    * start with the first node out of the queue, use pop to remove it too
        u = queue.pop(0)
        * for each of the weight connections of the first node,the i is the index of the node
            for i in range(len(graph[u])): 
            # if that node connection has not been visited and there is a weight value,
                if visited[i] == False and graph[u][i] >0:
                    # place that node index on the queue for the next value to check
                    queue.append(i)
                    # set that node to visited and update parent to prior value
                    visited[i]= True
                    parent=u


while queue : 
    u = queue.pop(0)

    for i in range(len(graph[u])):

         if visited[i] is False and graph[u][i] > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = u


Part 2 Ford Fulkerson
# initialize parents as all values of -1 and max flow to zero
# parameters graph, s, t
 
def ford_fulkerson(graph, s, t):
    parent = [-1] * len(graph)
    max_flow = 0 



"""





## find the maximum flow capacity : https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/ 


# the purpose of the BFS is to check if there are any paths left to run
# study more on what the BFS exactly does 
def BFS(graph, s, t, parent):
    # graph: 
    # s: Start Node, number int value index
    # t : Sink Node
    # parent  : parent list is used to keep track of the parent node of each visited node.
    # Return True if there is node that has not iterated.
    visited = [False] * len(graph)
    queue =[] 
    # set first item of queue to be start list
    queue.append(s)
    visited[s] = True

    while queue:
      print('BFS queue',queue)
      # return queue index 0 value
      u = queue.pop(0)
      print('u',u)
    
      print('graph[u]',graph[u])

      for i in range(len(graph[u])):
        print('i',i)
        print(visited)
        print('visited[i]', visited[i])
        print('graph[u][i]',graph[u][i])
        
        # the graph[u][i] aka the remaining weights are greater than zero
        # here we are not checking anything with capacities like minus or finding the min
        # we are simply just checking whether there is a cpacity or not
        if visited[i] is False and graph[u][i] > 0:
                queue.append(i)
                # set the visited to True
                visited[i] = True
                # 현재 check 했던 node 은 이제 parent 으로 setting 해준다.
                parent[i] = u

    # Ford-Fulkerson algorithm, the parent node of a
    #  given node represents the node through which we reached the given node while traversing an augmenting path in the residual graph.

    print('BFS',visited)
    print('t',t)

    return True if visited[t] else False


def FordFulkerson(graph, source, sink):
    # This array is filled by BFS and to store path
    parent = [-1] * (len(graph))
    max_flow = 0

    # as long as there is a path from the source to the sink
    # graph is a bad name, think of it as values of weights in the graph
    while BFS(graph, source, sink, parent):
        # Step 2 :  reiterate with updated paths
        path_flow = float("Inf")
        s = sink

        # Step 1 :  1 path while loop
        # 5 != 0 
        # this means for one path in the graph  this while loop will run
        # and find the min value of the path_flow
        while s != source:
            # Find the minimum value in select path
            # when we do parent[s][s] we are doing row, column
            # the rows and columns values contain the node

            #for first iteration
            print(s) #5 
            print(parent[s]) #3
            print(graph[parent[s]][s]) # weight of 3 --> 5
            print(path_flow) # inf, resets path_flow = 20
            print('-----')

            # for next iteraction
            # s = 3
            # parent[s]  =1 
            # graph[parent[s]][s] weight 3 -> 1 = 12
            # path_flow = 12
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        
        max_flow += path_flow
        v = sink
        print('max_Flow',max_flow)

        # 5 ! = 0 
        while v != source:
            u = parent[v]
            # update edges ran through
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            # update parent move up the path
            v = parent[v]

    # return the max flow for 1 path iteration
    print('1 iter',max_flow)
    return max_flow

graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]
source, sink = 0, 5
print(FordFulkerson(graph, source, sink))

# import networkx as nx
# import matplotlib.pyplot as plt
# import numpy as np

# Graph as an adjacency matrix


# Create a graph object
# G = nx.from_numpy_array(graph, create_using=nx.DiGraph)

# # Draw the graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', arrows=True)

# # Add edge weights labels
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Display the graph
# plt.show()



# first greedy algorithm - personally found it very hard