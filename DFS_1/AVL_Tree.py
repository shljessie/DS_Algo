"""
AVL tree is a self-balancing binary search tree
in which each node maintains extra information called 
a balance factor whose value is either -1, 0 or +1.

Balance factor (L_subtree - R_subtree  or  R_subtree - L_subtree)
 of a node in an AVL tree is the difference between
  the height of the left subtree and that of the right subtree
   of that node.

Left Rotate : https://www.programiz.com/dsa/avl-tree
The left rotation helps in rebalancing the tree by reducing 
the height difference between the left and right subtrees of
the pivot node. It preserves the binary search tree property,
where all elements in the left subtree of a node are less than 
the node, and all elements in the right subtree are greater than the node.

Right Rotate 

"""

import sys

class TreeNode:
   def __init__(self,key):
      self.key = key
      self.left= None
      self.right= None
      # initializing height to 1 is a convention
      self.height =1

class AVLTree(object):

   # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    #Function to insert a node
    def insert(self,root,key):
      if root is None:
         return self.Node(key)

      if key <root.key:
         root.left = self.insert(root.left,key)
      elif key > root.key:
         root.right = self.insert(root.right,key)
      
      # calculating the root height while considering itself
      root.height = 1 + max( max(self.getHeight(root.left),
                              self.getHeight(root.right)))

      # update the balance factor
      balanceFactor = self.getBalance(root)

      # left-right 이니까 this means tree is left heavy
      if balanceFactor > 1:
            if key < root.left.key:
                #This rotation moves the left child of the root node to the root position,
                #  making it the new root. The original root node becomes the
                #  right child of the new root.

                # simple: if the left is heavy, we do a right rotation
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

      # left-right 이니까 this means tree is right heavy
      if balanceFactor < -1:
         if key > root.right.key:
               # simple: if the right is heavy, we do a left rotation
               return self.leftRotate(root)
         else:
               root.right = self.rightRotate(root.right)
               return self.leftRotate(root)

      
   

