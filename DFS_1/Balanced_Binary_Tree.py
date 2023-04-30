"""
Balanced Binary Tree

(1) the difference between the left subtree and the right subtree is not greater than 0

we need to use a value of height to compare. 
using recursion, we find the height values of the subtrees

** the height has be an object

why? can't we just pass in left,right,current variables in each recursive call?
It would be the same in terms of the number of variables created, but using the Height object can reduce the number of parameters passed in the recursive function calls.

If you use individual variables for left height, right height, and current height, you would need to pass all three variables as arguments in each recursive call. This means that you need to allocate memory for all three variables in each call, which can result in a larger memory footprint.

On the other hand, using a single Height object reduces the number of arguments that need to be passed in each call. Since the same Height object is used throughout the recursion, there is no need to allocate additional memory for the object in each call. This can result in lower memory usage and improved performance.
"""

class Node:
  def __init__(self,val):
    self.val = val
    self.left , self.right = None , None
  
class Height:
  def __init__(self):
    self.height=0

def isBalanced(root,height):

  #base case when root is empty
  if root == None:
    return True

  # get left and right height
  left_height = Height()
  right_height = Height()

  # get height at any node
  l = isBalanced(root.left, left_height)
  r = isBalanced(root.right, right_height)

  #storing and updating current node with node height value
  height.height = max(left_height.height,left_height.height) +1 

  # if height different is smaller or equal to 1 continue on 
  if left_height.height - right_height.height <= 1: 
    return l and r

  # if height different is greater, return Flase
  return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.left.left = Node(4)
root.left.left.left.left = Node(4)
# root.left.right = Node(5)

# root.right.left = Node(6)
# root.right.right = Node(7)

height = Height()

if isBalanced(root, height):
  print('This is a Balanced Binary Tree')
else: 
  print('This is not Balanced')

