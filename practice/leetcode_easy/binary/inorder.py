# again using recursion for binary search trees
# look at the lump of the left subtree and the right subtree


# the code here is for simple printing 
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




# the code here is for storing
# after the recursion occurs, we also want to do additional storing of the values
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        

        output =[]
        if root:
            #traverser left
            output += self.inorderTraversal(root.left)

            # traverse root
            output += [root.val]

            # traverse right
            output += self.inorderTraversal(root.right)

            print(output)
        
        return output