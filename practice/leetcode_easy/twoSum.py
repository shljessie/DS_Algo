"""
Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

# my solution
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # for each index in range
    for i in range(len(nums)):
      if target - nums[i] in nums and nums.index(target - nums[i]) != i:
        return [i,nums.index(target - nums[i])]

    return []



# solution using index to check 
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numToIndex = {}
    for i in range(len(nums)):
        if target - nums[i] in numToIndex:
            return [numToIndex[target - nums[i]], i]
        numToIndex[nums[i]] = i
    return []

    # >> dictionary save as we go and check as we go, focus is on trying to remember past items

#brute force solution
def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
          for j in range(i + 1, len(nums)):
              if (i != j and nums[i] + nums[j] == target):
                  return [i, j]
      return []


#solution using enumerate : similar to the past solutions but just using a different value
def twoSum(nums, target):
  prevMap = {} # val : index
        
  for i, n in enumerate(nums):
      diff = target - n
      if diff in prevMap:
          return [prevMap[diff], i]
      prevMap[n] = i
  return