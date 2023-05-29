class Node:
  def __init__(self,data):
      self.data = data
      self.next = None
  
class LinkedList:
  def __init__(self):
      self.head= None
  
  def traverse(self):
      temp = self.head
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
  print(list.next)