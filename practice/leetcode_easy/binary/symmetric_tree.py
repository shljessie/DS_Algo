"""
Given the root of a binary tree, check whether
it is a mirror of itself (i.e., symmetric around its center).
https://leetcode.com/problems/symmetric-tree/description/

** 조금 어렵 다시 생각해보기!! recursion 공부
"""

def isSymmetric(self,root):

  def isMirror(root1, root2):
    if root1 == None and root2 ==None:
      return True
    
    if root1 is not None and root2 is not None:
      if root1.val == root2.val:
        return isMirror(root1.left,root2.right) and isMirror(root1.right, root2.left)
    return False

  return isMirror(self,root.left,root.right)
