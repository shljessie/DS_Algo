"""
The perfect binary tree uses the depth concept of nodes
depth starts top down 
so the root node has a depth of 0 

perfect binary tree conditions 
(1) all nodes have at least two children 
(2) all nodes look the same at the same level 
    ( all nodes have no children + the depth count is the same)

- start from top down count the depths 
- go through starting from root node 
"""

class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

#check the depth of the tree
def checkDepth(root):
    d = 0
    while (root is not None):
        d += 1
        root = root.left
    return d
  # d=0
  # # use while to continuously go through the loop when sth is true
  # while root:
  #   root = root.left
  #   d +=1
  # return d


# check if perfect Binary
def isPerfect(root, d, level=0):

  # base case when the root is empty 
  if root == None:
    return True

  # second case when both are empty
  if root.left == None and root.right == None: 
    return (d == level +1)

  # case when one is none and other is not, catch non perfect
  if root.left == None or root.right == None:
    return False

  #recursion case
  # print(isPerfect(root.left, d, level+1) and isPerfect(root.right,d ,level+1))
  return (isPerfect(root.left, d, level+1) and isPerfect(root.right,d ,level+1))


root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(2)
root.left.right = Node(2)

root.right.left = Node(2)
root.right.right = Node(2)

# print(isPerfect(root.left, d, level+1) and isPerfect(root.right,d ,level+1))
# print(isPerfect(root, checkDepth(root)))
if isPerfect(root, checkDepth(root)):
  print('This is a perfect Binary Tree')
else:
  print('This is not a perfect Binary Tree')
