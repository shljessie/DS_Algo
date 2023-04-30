"""
Binary Search Algorithm 

Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.

* It is called a binary tree because each tree node has a maximum of two children.
* It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.

- In easy terms, all nodes to the left are less than the root node, all nodes to the right are greater than the root node
"""

class Node:
  def __init__ (self,key):
    self.key = key
    self.left = None
    self.right = None

  
  # in order traversal
  def inorder(self,root):
    if root is not None:
      # Traverse Left
      self.inorder(root.left)
      # Traverse root
      print(str(root.key) + "->", end=" ")
      # Traverse right
      self.inorder(root.right)

  def insert(self,node,key):
    # node represents the current node in BST
    # key is the value we want to insert into the tree
    if node is None:
      return Node(key)
    
    if key < node.key:
      #move to left node to be current node and check again 
      # we do the assignment because if the left moved value is the new insert position,
      # we want to update it
      node.left = self.insert(node.left,key)
    else: 
      node.right = self.insert(node.right,key)
    
    # this return statements is for the parts where we moved left
    #  but it isn't the final insertion value
    return node

  # find the value of the leftmost node
  def minValueNode(self,node):
    # Find the leftmost leaf
    while(node.left is not None):
        node = node.left

    return node


  # when deleting the node, there are two scenarios to consider
  # When deleting a node from a Binary Search Tree (BST), there are three scenarios to consider:

  #If the node to be deleted has no children or only one child, it can be directly removed from the BST without any complications.

  #However, if the node to be deleted has two children, we need to choose a replacement node to maintain the BST structure. One common approach is to choose the inorder successor of the node to be deleted.
  
  def deleteNode(self,root,key):
    # key is the value of the node we want to delete
    # root is the starting point

    #base case
    if root is None:
      return root

    # find node to be deleted
    if key < root.key:
      root.left = self.deletenode(root.left, key)
    elif key < root.key:
      root.right = self.deletenode(root.right, key)
    else:
      # if the root is with only one child
      # if only one child, we want to delete the node and connect the child to the parent
      if root.left is None:
            temp = root.right
            root = None
            return temp

      elif root.right is None:
            temp = root.left
            root = None
            return temp

      # If the node has two children,
      # place the inorder successor in position of the node to be deleted
      # the inorder successor is the smallest value in the right subtree

      # By choosing the inorder successor, we ensure that the replacement node
      #  is greater than all nodes in the left subtree (as it is greater than the node being deleted)
      #  and less than all nodes in the right subtree (as it is the smallest node in the right subtree).
      temp = self.minValueNode(root.right)

      root.key = temp.key

      # Delete the inorder successor
      root.right = self.deleteNode(root.right,temp.key)

# the deleteNode function returns the reference to the updated root node of the modified BST after deleting a node.
    return root



root = Node(8)
root = root.insert(root, 8)
root = root.insert(root, 3)
root = root.insert(root, 1)
root = root.insert(root, 6)
root = root.insert(root, 7)
root = root.insert(root, 10)
root = root.insert(root, 14)
root = root.insert(root, 4)


print("Inorder traversal: ", end=' ')
root.inorder(root)

print("\nDelete 10")
root = root.deleteNode(root,8)
print("Inorder traversal: ", end=' ')
root.inorder(root)