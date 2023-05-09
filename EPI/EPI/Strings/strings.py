"""
<common operations with strings>
comparison, joining, splitting, searching for substrings, replacing one string
by another, parsing,
>> s[3], len(s), s + t, s[2:4] 
>> s in t, s.strip(): removes whitespace,
>> s.startswith(prefix[string]), s.endswith(suffix)
>> s.lower(), s.upper() , s.isupper(), s.islower()

>> .join()  // # join elements of text with space ' '.join(text)
>> # .join() with lists
>> numList = ['1', '2', '3', '4']
>> separator = ', '
>> print(separator.join(numList))
>> a.join(b) --> ab
>> b.join(a) --> ba

* remove value in string
>>  s.replace()
>> 이건 없음! .drop() , .replace() ..etc

*sort a string
>> sorted(s1) sorted(s2)

>> txt = "For only {price:.2f} dollars!"
>> print(txt.format(price = 49))

<how strings are represented in memory>
how strings are represented in memory, 

<strings are immutable> (below is what it means by saying strings are immuatable)
You cannot try to change a particular
character or set of characters within a string without completely replacing the string.


** new fact ~ : refers to inverse
** The all() function returns True if all items in an iterable are true, otherwise it returns False.
"""

# palidrome : read the same forwards and backwards
def palindrome(s):
  return all(s[i] == s[~i] for i in range(len(s)//2))

# 여기서 10문제! 
#https://medium.com/javarevisited/top-21-string-programming-interview-questions-for-beginners-and-experienced-developers-56037048de45

# anagram
def anagram(s1,s2):
  if len(s1)!=len(s2):
    return False

  for i,j in zip(s1,s2):
    if i in s2 and j in s1: 
      s1 = s1.replace(j,' ')
      s2 =s2.replace(i,' ')
    else:
      return False
  return True

#anagram sol 2
def anagram2(s1,s2):
  if sorted(s1) == sorted(s2):
    return True
  return False

#test anagram 
# s1="erca"
# s2="raced"
# p= anagram2(s1,s2)
# print(p)


#reverse a string 
a='asdf9c'
# move by step -1, which is moving backwards
reversed_string = a[::-1]
# python reversed returns a reversed object
# print(reversed(a))



#print duplicates
a= 'asdasdasdasddo2'
from collections import Counter
ac = Counter(a)
# loop through counter key
dup =[]
for key in ac:
  if ac[key] >1 and key not in dup:
    dup.append(key)

print(dup)
# time complexity : O(n^2) 
# set returns the unique values
# print(ac)


# print duplicates non Counter solution
# range is O(n) time complexity so try not to use it if possible
uni =[]
dup = []
for i in a:
  if i not in uni:
    uni.append(i)
  elif i not in dup:
    dup.append(i)
print(dup)


# all combinations of string
a= 'asdasdasdasddo2'

# more intuitive solution, two combinations
per=[]
for i in range(len(a)):
  for j in range(1,len(a)):
    per.append(a[i]+a[j])

# print(per)


# permutations mean the differet combinations we can
# get from that string, same length
# faster solution --> recursion

# you need to understand the tree image
# the reason we swap.

com =[] 

def permutation(a,l,r):
  if l ==r: 
    com.append(a)
  for i in range(l,r):
    a[l], a[i] = a[i], a[l]
    permutation(a, l+1, r)
    a[l], a[i] = a[i], a[l] 
    # backtrack, so that other permutation combintations can operate on the original
    # leaving this for the second tree group
  return com

def permutation_size(a,l,r,n):
  if l ==r: 
    com.append(a)
  for i in range(l,r):
    a[l], a[i] = a[i], a[l]
    permutation_size(a, l+1, r,n)
    a[l], a[i] = a[i], a[l] 
    # backtrack, so that other permutation combintations can operate on the original
    # leaving this for the second tree group
  return com

    

# really easy solution
# itertools.permutations :https://stackoverflow.com/questions/46846978/generate-all-permutations-of-fixed-length-where-the-elements-come-from-two-diffe


# find all substrings 

# string segmentaion

# Google Example Coding questions : https://igotanoffer.com/blogs/tech/google-software-engineer-interview#coding