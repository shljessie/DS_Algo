# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/2406277/python-easily-understood-faster-than-86-less-than-83-recursion/ 
# sorted, can start from the middle 
# we want to continuous repeat the action of finding the middle nums value --> recursion problem

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if len(nums)==0:
            return None 

        root = len(nums) //2

        return TreeNode(
            nums[root], 
            self.sortedArrayToBST(nums[:root]), 
            self.sortedArrayToBST(nums[root+1:])
            )