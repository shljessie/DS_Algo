"""
Given a string s, find the length of the longest 
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

## Hashtable solution
def lengthOfLongestSubstring(s: str) -> int:
    ans =''
    final =[] 

    if len(s) ==0 :
      return 0

    for i in s:
      print(i)
      if i not in ans:
        ans = ans + i
      elif i in ans:
        final.append(ans)
        ans = i
      
      # final.append(ans)

    print('final',final)

    return len(max(final,key=len))


## to use the max function on a list of srings, always define a key value.          
s = "pw"
# ans = lengthOfLongestSubstring(s)
# print(ans)


def lengthOfLongestSubstring(s: str) -> int:
        hash={}

        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]] = 1
            else:
                hash[s[i]] +=1

        print(hash)

"""
>>> for i in enumerate(b[0]):
...     print(i)
... 
(0, 'a')
(1, 's')
(2, 'd')
(3, 'f')
"""

s = "pwaspw"
ans = lengthOfLongestSubstring(s)
print(ans)



"""
Identify that this is a Sliding window problem
"""
s = "pwaspw"

# Sliding window basic example

# Example: Given an array of integers of size ‘n’,
# Our aim is to calculate the maximum sum of ‘k’ consecutive
# elements in the array.

#https://www.youtube.com/watch?v=wiGpQwVHdE0

