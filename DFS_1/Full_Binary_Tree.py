
"""
A full Binary tree is a 
special type of binary tree
 in which every parent node/internal
  node has either two or no children.
"""
class Node:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.val = value

def isFullBinary(root):

  #Base case when empty Tree
  if root.val == None:
    return True
  
  #Base case when bottom leaves have no children left 
  if root.left == None and root.right == None:
    return True


  #Recursive Case 
  if root.left != None or root.right!=None:

    return isFullBinary(root.left) and isFullBinary(root.right)
    # we make recursive calls inside return statements 
    # It allows you to return a value directly from the 
    # recursive call. If you make the recursive call in the 
    # function body, you would need to store the result in a 
    # variable and then return that variable at the end of the function. 

  return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# IMPortnat !! check the return type: the return type of this function is a Boolean
# it will not print out statements. We need to define a secondary action that 
# this isFullBinary function will take.
if isFullBinary(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")