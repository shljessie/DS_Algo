# Data Structures and Algorithms

A Self-Tracked Study of Data Structures and Algorithms

Full Implementation of Code of Data Structures and Algorithms


### Videos on Good Tips for Coding Interviews

1. Steps for solving Leetcode Problems and how to approach them.
https://www.youtube.com/watch?v=xF554Tlzo-c 
- start with easy leetcode problems alongside reviewing datastructures and algorithms

2. Think of the solution first before you go on to code the problem
- when thinking of the solution, you are not thinking about how to code the solution.
- humans cannot multi task don't think of the code solution first!
- train your brain to think separately about how to come up with the solution and how to code
- (spends about 15min coding the solution, the rest goes into thinking about the solution)

3. Spend only an hour thinking about the solution to the problem
- Always go through and read the top solutions

4. You are ready when --> you can solve any new problem you encounter well
- you can consistently solve leetcode medium level questions in less than 30,40 minutes
 
5. Finally review!
- spend a good amount of time reviewing what you learned and what problems you solved.


## Study Plan 

## May 2023
- Review Data Structures and Algorithms + Finish all Leetcode Easy questions (30 easy questions)
https://leetcode.com/problem-list/top-interview-questions/?difficulty=EASY&page=1 

## June 2023
- Start solving Leetcode medium questions + and constantly review each topic , one topic one day


## July 2023 
-
### 1. DFS_1 = Depth First Search 

- Binary Tree  
- Full Binary Tree : Every Parent has two or no children
- Perfect Binary Tree : Every node has two children and are at same level
- Complete Binary Tree : All levels are filled and lean to the left
- Balanced Binary Tree : A balanced binary tree, also referred to as a height-balanced binary tree, is defined as a binary tree in which the height of the left and right subtree of any node differ by not more than 1.
- Binary Search Tree : smaller to left, larger to right. Insert and Deletion (Olog(n) time)
- AVL Tree : Root has an additional balance value, and we want to balance the tree alonside inserting and dleeting items in the tree. Left and Right rotation.


### 2. Greedy Algorithms

  ~ * small sidenote (living by the greedy algorithm)

    1. Let's start with the root node 20. The weight of the right child is 3 and the weight of the left child is 2.

    2. Our problem is to find the largest path. And, the optimal solution at the moment is 3. So, the greedy algorithm will choose 3.

    3. Finally the weight of an only child of 3 is 1. This gives us our final result 20 + 3 + 1 = 24.

    However, it is not the optimal solution. There is another path that carries more weight (20 + 2 + 10 = 32) as shown in the image below.


* Ford Fulkerson Algorithm
- Important Concepts : graph 2D form to Node Graph Form , BFS Function Coding , Ford Fulkerson Algo, Understand Overall Architecture of Implementing the Algorithm to Code.

<img width="441" alt="Screen Shot 2023-05-03 at 5 18 53 PM" src="https://user-images.githubusercontent.com/59305253/235950839-55673211-e092-4a6c-9684-17d40bbe8604.png">

### 3. Array

I've organized a list of basic array operations and the meaning of creating copy() deepcopy() ...etc in arrays. Would be great to review before doing coding interviews.



### 4. Linked List 

Basic Reviews on what Linkedlists return
return(LinkedList) returns an array [1,2,3,4]
What does it mean for two variables to have pointers to the same linked list?
How can we leverage this to keep track of one linkedlist. next value we needt obtain?

* Sample Image below on Merging two sorted linked lists
- important concepts
- cur.next = list1 updates the next reference of the current node.
  - cur.next = list1 modifies the shared ListNode object that cur and dummy are both pointing to, while cur = list1 reassigns cur to a new ListNode object, independent of dummy.

- cur = list1 moves the cur pointer to the next node in the merged list.
  - when you update cur = list1, you are changing the reference that cur holds. After this assignment, cur will point to the ListNode object that list1 is currently pointing to, while dummy still maintains its reference to the original ListNode object.


### Coding Practice Tracker 
https://docs.google.com/spreadsheets/d/1IWPaT8uZyOwmcdzuiEixordCl90_NnXGYJ0aJYTte_w/edit#gid=0


### 5. Binary Trees

Binary trees deal with a lot of problems involving recursion! 
Indentify the recursion problem by noticing the repeated actions.
Then think of how the output is being returned : is the value at the end of the recurison enough or should I add 1 to it? / am i storign the outputs of my recursion?
how should i set the base case for my recursion?