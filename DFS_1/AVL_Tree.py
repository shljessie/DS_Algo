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



Big Steps 
1. do insertion and deletion as before
2. but then think about the balance
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
         # just returning the root.height
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
         # minus the root.left - root.right
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
      root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

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

      return root

      
    def getMinValueNode(self, root):
      # 가장 왼편에 있는 node 을 찾고 싶은 것, 계속 왼쪽으로 이동시켜 주기
      if root is None or root.left is None:
            return root
         
      return self.getMinValueNode(root.left)

   
    def delete(self, root, key):
      #if there is nothing to delete just return the root.
      if root is None:
         return root
      
      if key < root.key: 
         root.left = self.delete(root.left, key)
      elif key > root.key:
         root.right = self.delete(root.right, key)
      else: 
         # if the key is the same
         # if the node has one child
         if root.left is None:
            temp = root.right
            root = None
            return temp
         
         elif root.right is None:
            temp = root.left
            root = None
            return temp

         # if the node has two children
         #get smallest node in right tree
         temp = self.getMinValue(root.right)
         # replace that with current node
         root.key = temp.key 
         # delete that smallest node in right tree
         self.delete(root.right, temp.key)

      
      # now we think about the balance
      # height
      root.height = 1+ max(self.getHeight(root.left),
                              self.getHeight(root.right))

      # update blaance factor
      balanceFactor = self.getBalance(root)

      # left heavy
      if balanceFactor > 1 : 
         if key < root.left.key:
            return self.rightRotate(root)
         else: 
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
         
      # right heavy
      elif balanceFactor < -1: 
         if key > root.right.ley:
            return self.leftRotate(root)
         else:
            root.left = self.rightRotate(root.left)
            return self.leftRotate(root)
      
      return root

    def leftRotate(self, z):
      y = z.right
      T2 = y.left
      y.left = z
      z.right = T2
      z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
      y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
      return y

      
    def rightRotate(self, z):
      y = z.left
      T3 = y.right
      y.right = z
      z.left = T3
      z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
      y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
      return y


      
   

