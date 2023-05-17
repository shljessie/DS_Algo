"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
"""


class Solution(object):
    def maxDepth(self, root):
      """
      type root: TreeNode
      """

      if root is None:
        return 0
      
      return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
# at the end, Max(0,0)+1 so the bottom node gets a value of 1 which is what the upper node self.maxDepth(root.right) would be getting


"""
The maxDepth function is called with the root node TreeNode(3).
  The root node is not None, so the code continues.
  The maxDepth function is recursively called for the left and right subtrees.
    self.maxDepth(root.left): This is called with TreeNode(9) as the root of the left subtree.
      The root node is not None, so the code continues.
        TreeNode(9) has no children, so the function returns 0.
    self.maxDepth(root.right): This is called with TreeNode(20) as the root of the right subtree.
      The root node is not None, so the code continues.
      The maxDepth function is recursively called for the left and right subtrees of TreeNode(20).
        self.maxDepth(root.left): This is called with TreeNode(15) as the root of the left subtree.
        The root node is not None, so the code continues.
        TreeNode(15) has no children, so the function returns 0.
        self.maxDepth(root.right): This is called with TreeNode(7) as the root of the right subtree.
  The root node is not None, so the code continues.
    TreeNode(7) has no children, so the function returns 0.
  The max function compares the depths of the left and right subtrees: max(0, 0), which returns 0.
  The max function in the initial call to maxDepth compares the depths of the left and right subtrees: max(0, 0), which returns 0.

"""