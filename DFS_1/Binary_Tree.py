"""
As an extension of the DFS search algorithms,
you can define binary tree search algorithms as depth first search or not
"""

class Node:
  def __init__(self, key):
    self.left = None
    self.right= None
    self.val = key 

  def preorder(self):
    if self:
      #Traverse current
      print( str(self.val))
    
    # we also have to additionally start defining conditions
    if self.left:
      #Traverse left  : only difference is that we don't do preorder(self.left) --> we do self.left.preorder()
      # this function is an instance function a function defined inside a class
      # By convention, the first parameter of instance methods is always named self. 
      # This is because self is not a reserved keyword in Python, but using this name helps make it clear that the parameter represents the instance of the class. 
      self.left.preorder()
    if self.right:
      #Traverse right
      self.right.preorder()

#this makes sense for different instance calss inside of python

root = Node(1)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(8)

root.preorder()