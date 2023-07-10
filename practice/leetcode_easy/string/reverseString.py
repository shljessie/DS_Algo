"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.


reverse() actually reverses the elements in the container. reversed() 
doesn't actually reverse anything, it merely returns an object that can 
be used to iterate over the container's elements in reverse order.

"""

# reversed(list) => returns an object but doesn't really reverse the original string
# list.reverse() reverses the list 
# use [::-1] to actually be able to reverse the list and create a new element 


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return s.reverse()