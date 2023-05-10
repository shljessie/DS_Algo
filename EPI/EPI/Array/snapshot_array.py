# Google Example Coding questions : https://igotanoffer.com/blogs/tech/google-software-engineer-interview#coding

# Snapshot array : https://leetcode.com/problems/snapshot-array/solutions/

"""
Implement a SnapshotArray that supports the following interface:

* SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
* void set(index, val) sets the element at the given index to be equal to val.
* int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
* int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""

class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.snap_save= {}
        self.snap = [0] * length
       
    
    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.snap[index] = val
        return self.snap
        

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id +=1
        self.snap_save[self.snap_id] =  self.snap.deepcopy()

        return self.snap_id


    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # find snap_id at given time
        val=self.snap_save[self.snap_id]
       

        return  val[index], self.snap_id


# Your SnapshotArray object will be instantiated and called as such:

import bisect

class SnapshotArray(object):
    def __init__(self, n):
        self.cache = [[[-1, 0]] for _ in range(n)]
        self.i = 0

    def set(self, index, val):
        self.cache[index].append([self.i, val])

    def snap(self):
        self.i += 1
        return self.i - 1

    # @lru_cache(maxsize=None)
    def get(self, index, snap_id):
        i = bisect.bisect(self.cache[index], [snap_id + 1]) - 1
        return self.cache[index][i][1] 



## !! Solution
class SnapshotArray:
    def __init__(self, length: int):
        self.cache = []
        self.d = dict()
        self.i = 0

    def set(self, index: int, val: int) -> None:
        self.d[index] = val

# * int snap() takes a snapshot of the array and 
# returns the snap_id: the total number of times we called snap() minus 1.
    def snap(self) -> int:
        self.cache.append(dict(self.d))
        self.i += 1
        return self.i-1

# * int get(index, snap_id) returns the value at the given index, 
# at the time we took the snapshot with the given snap_id
    def get(self, index: int, snap_id: int) -> int:
        print('cache',self.cache)
        # self.cache is a list of dictionary items
        snap = self.cache[snap_id] # gets snap_id dictionary item
        print(snap)
        return snap[index] if index in snap else 0

# if index in snap, checks if there is a key in the dictionary , meaning if a key with the index value exits, retur nthe value in the dictionary

snapshotArr = SnapshotArray(3)
print(snapshotArr.cache)
snapshotArr.set(0,5)
snapshotArr.snap()
print(snapshotArr.cache)
print(snapshotArr.i)
snapshotArr.set(0,6)
snapshotArr.snap()
# snapshotArr.get(0,0)
print(snapshotArr.get(0,0))
print(snapshotArr.get(0,1))