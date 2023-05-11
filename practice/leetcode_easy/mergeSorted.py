"""
MergeTwo Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# My Solution = Times out!
def mergeTwoLists(list1, list2):

  ans =[]

  while list1.val or list2.val:
    if list1.val <= list2.val:
      ans.append(list1.val)
      if list1.next:
        list1 = list1.next
    else: 
      ans.append(list2.val)
      if list2.next:
        list2 = list2.next

  return ans


# Need to know some important facts about linkedlists
# if you return a LinkedList, you get a list value, not ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}}}}
# You can create a linkedlist instance by calling ListNode()
# When you first initialize ListNode, you get ListNode{val: 0, next: None}


# My Solution = Times out!
def mergeTwoLists(list1, list2):

  ans =ListNode()

  while list1 or list2:
    if list1.val <= list2.val:
      ans
      if list1.next:
        list1 = list1.next
    else: 
      ans.append(list2.val)
      if list2.next:
        list2 = list2.next

  return ans


# Solution Study = Using Linked List Data Structure 
# Since returning linked list returns a list array

# for example, list1 = [1,2,4] and list2 = [1,3,4]

# the goal here is to update the dummy.next with the sorted order

############
# cur is the pointer to where the dummy should be appended
############

def mergeTwoLists(list1, list2):

  # At the beginning the curr and the dummy point to the same node
  curr = dummy = ListNode()
# step1 
# curr = ListNode{val: 0, next: None}
# dummy = ListNode{val: 0, next: None}

  while list1 and list2:
    if list1.val < list2.val: 
      curr.next = list1
      # step4 
      # ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}}
      # ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}}}
      list1, cur = list1.next, list1

    else: 

      curr.next = list2
      # step2 - updating the curr.next updates both the dummy and curr
      # cur:  ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
      # dummy : ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}

      list2,cur = list2.next,list2
      # step3 - the pointer of cur is updated (cur = list2) , so now dummy and cur have different values
      #ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
      #ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}

  

## Questions
# 1. What does it mean for two variables to have pointers to the same linked list?
# >>> when two variables have pointers to the same linked list, it means that both 
# >>> variables are referring to the same underlying linked list structure in memory. 
# >>> Any modifications made to the linked list through one variable will be visible 
# >>> when accessing it through the other variable.

# Review the concept behind merging two linked lists : https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/ 
