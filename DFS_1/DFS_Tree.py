

"""
Three Functions of Depth First Search

1. Preorder : current tree -> left tree -> right tree
2. In order : left tree -> current -> right tree 
3. Post order : left tree -> right tree -> current tree

"""
class Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.val = item 
    
def inorder(root): 
    #the root becomes the current 
    if root:
        #Traversal Left tree *which is why this is recursive
        inorder(root.left)
        #Traversal current 
        print(str(root.val) +' ==> ')
        #Traversal right 
        inorder(root.right)

def preorder(root):
    if root:
      #Traversal current
      print(str(root.val) +' ==> ')
      #Traversal left 
      preorder(root.left)
      #Traversal right
      preorder(root.right)

def postorder(root):
    if root: 
        #Traversal left
        postorder(root.left)
        #Traversal right 
        postorder(root.right)
        #Traversal current
        print(str(root.val) +' ==> ')

# mistake... below but good for understandinf function of self
# self is a reference to the instance of a class on which a method is being called, 
#In object-oriented programming, an instance is a specific occurrence of a class. 
# whe we call a class once, like in the root=Node(1) line below, root becomes one instance of a class
# by calling self in the inorder fucntion inside the Node class, we are calling that root instance and going through the function in that root instance again.

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)