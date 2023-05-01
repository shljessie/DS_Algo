"""
Binary Search Tree

left small, right larger
"""

class Node():
  def __init__(self,key):
    self.key = key
    self.left = None
    self.right = None

  def inorder(self, root):
    # 그냥 node 3개 있는 tree 가 있었다고 할때, left --> right 까지 traverse 하는것
    if root is not None:
      # Traverse left
      self.inorder(root.left)

      # Print value
      print( str(root.key) + "->" )

      # Traverse right
      self.inorder(root.right)
  
  def insert(self,node,key): 
    # node represents the current node in the binary tree 
    if node is None: 
      # WHERE the insertion happens!!!
      #  계속 더 작은,혹은 더 큰 node을 찾다가 더이상 node 이 없다면 그 위치에 새롭게 생성
      # 그냥 이렇게 Node(key) 하면 바로 생성할 수 있음.
      return Node(key)
    
    if key < node.key:
      # change the current node to the left node and do the insertion
      node.left = self.insert(node.left ,key)
    elif key > node.key: 
      node.right = self.insert(node.right, key)
    
    # return the final updated value of the node
    # the return statement is placing values! 
    print(node.right)
    return node

  def visualize(self, level=0):
      if self.right:
          self.right.visualize(level + 1)
      print('    ' * level + '|---', self.key)
      if self.left:
          self.left.visualize(level + 1)


  def delete(self,node,key):
    # node is the current node we are at key is the value we wnat to delete

    if node is None:
      # if there is nothing to delete, just return the orignial value
      return node
    
    if key < node.key: 
      node.left= self.delete(node.left,key)
    elif key > node.key:
      node.right = self.delete(node.right,key)
    else:
      # if the key is the same as the current node,
      # we need do something that reorders the nodes
      if root.left is None:
            #store temp
            temp = root.right
            #delete node
            root = None

            # this returned temp value is going to get stored in the
            # node.left, node.right from above
            return temp

      elif root.right is None:
            #store temp
            temp = root.left
            root = None
            return temp


root = Node(8)
root = root.insert(root, 8)
root = root.insert(root, 3)
root = root.insert(root, 1)
root = root.insert(root, 6)
root = root.insert(root, 7)
root = root.insert(root, 10)
root = root.insert(root, 14)
root = root.insert(root, 4)

# root.inorder(root)
root.visualize()

