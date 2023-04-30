"""
Complete Binary Tree
1. All the nodes are leaning left
2. All the nodes before the last level are filled. 

complete binary trees are solved using 
1. the complete number of nodes on the tree
2. comparing whether the index of a current node is 
greater than or equal to the num nodes in a tree (if it is it skipped a node val and is not a complete tree)


for example 
      0
    /   \
   1     2
  / \   /
 3   4 5
/
6


here at node 2, the index of the right node would be 2*2+2 =6 
but 6 >= numNodes(6) .
If the graph above fulfilled the complete binary tree conditions, 


"""

class Node:
  def __init__(self, val):
    self.left , self.right = None , None
    self.val = val
  
# Count nodes 
def countNodes(root):
  if root == None:
    return 0 

  # use recursion to count values but remember!!! 
  return (1+countNodes(root.left)+countNodes(root.right))

def isComplete(root,index,numNodes):
  # base case when root is empty
  if root==None: 
    return True
  
  # when index number is skipped (check on Chatgpt for viz clarification)
  if index >= numNodes:
    return False
  
  # perform recursion 
  return isComplete(root.left, 2*index+1, numNodes) and isComplete(root.right, 2*index+2, numNodes)
  

root=Node(1)
root.left=Node(2)
root.right=Node(3)

root.left.left=Node(4)
root.left.right=Node(5)

root.right.left=Node(6)

index =0 
numNodes = countNodes(root)

if isComplete(root, index , numNodes):
  print('Yes this is a Complete Binary Tree')
else:
  print('No this is not a complete binary tree')

