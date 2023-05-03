# Data Structures and Algorithms

A Self-Tracked Study of Data Structures and Algorithms

Full Implementation of Code of Data Structures and Algorithms

### 1. DFS_1 = Depth First Search 

- Binary Tree  
- Full Binary Tree : Every Parent has two or no children
- Perfect Binary Tree : Every node has two children and are at same level
- Complete Binary Tree : All levels are filled and lean to the left
- Balanced Binary Tree : A balanced binary tree, also referred to as a height-balanced binary tree, is defined as a binary tree in which the height of the left and right subtree of any node differ by not more than 1.
- Binary Search Tree : smaller to left, larger to right. Insert and Deletion (Olog(n) time)
- AVL Tree : Root has an additional balance value, and we want to balance the tree alonside inserting and dleeting items in the tree. Left and Right rotation.


### 2. Greedy Algorithms

* small sidenote (living by the greedy algorithm)

1. Let's start with the root node 20. The weight of the right child is 3 and the weight of the left child is 2.

2. Our problem is to find the largest path. And, the optimal solution at the moment is 3. So, the greedy algorithm will choose 3.

3. Finally the weight of an only child of 3 is 1. This gives us our final result 20 + 3 + 1 = 24.

However, it is not the optimal solution. There is another path that carries more weight (20 + 2 + 10 = 32) as shown in the image below.

Overall Lesson : Don't be so sad that things didn't work out the way you expected there can be better things that wait ahead.