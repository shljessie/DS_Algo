"""
Given a string s, find the length of the longest 
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""


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
ans = lengthOfLongestSubstring(s)
print(ans)
