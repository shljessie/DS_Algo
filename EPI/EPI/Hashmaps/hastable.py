"""
Hashtable

A hash table is a data structure used to store keys, optionally, with corresponding values. Inserts,
deletes and lookups run in O(1) time on average.

take O(1) time to compute, on
average, lookups, insertions, and deletions have O(1+n/m) time complexity, where n is the number
of objects and m is the length of the array

"""

# Common Hashmap Problem = Anagrams
import collections

def find_anagrams(dictionary):
  # sets default value of dictionary to empty list
  sorted_string_to_anagrams = collections.defaultdict(list)

  for s in dictionary:
    # Sorts the string , uses it as a key , and then appends the original
    # string as another value into hash table.
    sorted_string_to_anagrams[''.join(sorted(s))].append(s)

  return [group for group in sorted_string_to_anagrams .values () if len(group) >= 2]


## collections.defaultdict 
# Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object.
#  The functionality of both dictionaries and defaultdict are almost same except for the fact
#  that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.


# value within default dict should be list or callable function
sorted_string_to_anagrams = collections.defaultdict(list)
print(sorted_string_to_anagrams['a'])