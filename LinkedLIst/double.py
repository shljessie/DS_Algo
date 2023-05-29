class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.next = next  # reference to next node in DLL
        self.prev = prev  # reference to previous node in DLL
        self.data = data


class DoubleLinked:

  def __init__(self):
    self.head= None
  
  # add node to front
  def front(self, new):
    newNode = Node(new)
    newNode.prev = None
    newNode.next = self.head

    # link prev of current head to new node
    if self.head:
      self.head.prev = newNode
    
    # assign the newNode to the head
    self.head = newNode
  
  # insert a node after a node
  def insertAfter(self, prev_node, new_data):

    # create new Node
    newNode=Node(new_data,prev_node)
    newNode.next = prev_node.next

    # prev_node.next
    prev_node.next = newNode

    # update the next values
    if newNode.next:
      newNode.next.prev = newNode

  def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == '__main__':
  linked_list = DoubleLinked()
  linked_list.head = Node(1)
  node2 = Node(2)
  node3 = Node(3)

  linked_list.head.next = node2
  node2.prev = linked_list.head
  node2.next = node3
  node3.prev = node2

  # Display the initial linked list
  linked_list.display() 

  # Insert a new node after the second node
  linked_list.insertAfter(node2,2.1)

  # Display the updated linked list
  linked_list.display() 