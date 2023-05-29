## Linked List

#### Basic Structure
-  Data(value) --> Next
- def Node(self, data) : 
    - data.val = data 
    - data.next = None

#### Why?
- The size of the array is fixed. **We never run out of memory space for linked lists** But we do for arrays because they are fixed sized.

- **Insertion/Deletion** : To insert new elements into the array, we have to shift values and make space.
- With linked lists, we can traverse the data structure and insert values. We do not need to shift values but simply change pointers

#### Traversal of a Linked List
```
class Node:
  def __init__(self,data):
      self.data = data
      self.next = None
  
class LinkedList:
  def __init__(self):
      self.head= None
  
  def traverse(self):
      temp = self.head:
      while (temp):
        print(temp.data)
        temp = temp.next

  
# Code execution starts here
if __name__ == '__main__':
  list = LinkedList()

  valOne = Node(3)
  valTwo = Node(2)
  valThree = Node(1)
  list.head = valOne
  list.head.next = valTwo
  list.head.next.next = valThree

  print(list.traverse())
    
```

- To assign values to the next, we have to reference the Node. So we need to do Node.next compared to just calling the linkedlist.next.
- In the linked list class, there is not value next. it just has the head and that is where we assign nodes.
- To get that node, and add a value to the next, we have to reference that Node and then call next.
- So when we do assignments, we call Node.next. The Node here is Linkedlist.head, Linkedlist.head.next, and Linkedlist.head.next.next


#### Space and Time Complexity
* Search - O(n), we have to traverse the list to find values
* Insert, Delete - O(1) we just need to change pointers
* Space O(n)


#### Applications
- Can be used to implement stacks and queues
- Can be used to implement hashtables



### Types

1. Double Linked List
```
class Node(self,data,next,prev):
  self.data = data
  self.prev = prev
  self.next = next 


class DoubleLinked:
  def __init__(self):
    self.head= None
  

  def frontadd(self,new):

    # create new node
    newNode = Node(new,self.head,None)

    # update prev of current head to newNode
    self.head.prev = newNode

    # update self.head
    self.head = newNode

  def insertAfter(self,prev_node, new):

    #create new node
    newNode = Node(new, prev_node, prev_node.next)

    # update prev_node
    prev_node.next = newNode

    # update next node
    new_node.next.prev = newNode

```


**Insert After** 

prev_node --> node to add --> next_node

1. create the new node & connect next and prev values
2. update the prev.next and next.prev values (check of next value exists) (the nodes front and back of the new node)

- time complexity : O(1)
- Space : O(1)

- In the example code, by passing prev_node as the prev_node parameter in the insertAfter method, you have direct access to that specific node, and you don't need to traverse the linked list to find it.Direct access means that we can specifiy after which node we want something to be inserted. If we ahve that information, we do not need to specify other things


**Delete After** 


prev_node --> node to delete --> next_node

1. update the node to delete's prev_node and next_node values. The prev_node.next should point to the next_node. and the next_node.prev should point to the prev_node.

```
  def deleteAfter(self,delete):
    prev_node.next = delete.next
    next_node.prev = delete.prev
```

This is correct but we need some checks! There are cases when the node to delete is the head node, the main node , or the next node.
for next time : https://www.geeksforgeeks.org/delete-a-node-in-a-doubly-linked-list/

