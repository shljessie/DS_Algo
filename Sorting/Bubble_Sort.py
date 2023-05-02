"""
Bubble sort is a sorting algorithm that compares

two adjacent elements and swaps them until they are in the intended order.

bubbleSort(array)
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
end bubbleSort

"""

# longer solution
def bubbleSort(array):
  for i in range(len(array)):
    for j in range(0,len(array) -i-1):
      if array[j] > array[j+1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1]= temp

  return array

# shorter solution
