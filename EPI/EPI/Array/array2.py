"""
Dutch National Flag Problem - Quicksort, Pivot

Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[i] (the “pivot”) appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.

1. partion problem to three groups : lower=0, middle=0, high=n-1 
2. while loop till middle index reaches high 

<this is not about sorting in order, this is about sorting from pivot> 
Generalizing, suppose A = h0, 1, 2, 0, 2, 1, 1i, and the pivot index is 3. Then A[3] = 0, so
h0, 0, 1, 2, 2, 1, 1i is a valid partitioning. For the same array, if the pivot index is 2, then A[2] = 2, so
the arrays h0, 1, 0, 1, 1, 2, 2i as well as h0, 0, 1, 1, 1, 2, 2i are valid partitionings


Quicksort is good when the pivot element is an intermediate value obtained by finding the median
when memory is costly,
"""

def dutch_flag_partition (pivot_index , A):
  pivot = A[pivot_index]
  l = 0
  m = 0
  h = len(A)-1

  while m < h:
    if A[m] < pivot : 
      A[l], A[m] =A[m], A[l]
      l += 1 
      m +=1 
    elif A[m]== pivot : 
      m +=1
    else: 
      A[m],A[h] = A[h],A[m]
      h -=1

  return A


def dutch_flag_partition_color(array):
  l = 0 
  m = 0
  h = len(array)-1 #check 
  while m < h: # check 
    if array[m] == 0 :
      array[l], array[m] = array[m],array[l]
      l +=1 
      m +=1
    elif array[m] ==1:
      m+=1
    else:
      array[h], array[m] = array[m],array[h]
      h -=1
  return array

# array = [0,1,2,3,1,3,2,4,1,2,0]
Array = [2,0,2,1,1,0]

a = dutch_flag_partition_color(Array)
print(a)
  
