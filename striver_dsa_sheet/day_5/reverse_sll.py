class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

class SLinkedList:
    def __init__(self):
        self.head = None 

    def push(self, val):
        if not self.head: self.head = Node(val)
        else:
            curr = self.head 
            while curr.next:
                curr = curr.next 
            curr.next = Node(val)
    def printList(self, head):
        curr = head
        while curr:
            print(curr.val, end = " ")
            curr = curr.next  
    def reverse_iter(self, node):
      prev = None 
      curr = node 
      while curr:
        next = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next 
      self.head = prev 
      
    def reverse_recer(self,node):
      if not node or not node.next:
        return node
      newNode = self.reverse_recer(node.next)
      nodeNext = node.next 
      node.next = None 
      nodeNext.next = node 
      return newNode
    
obj = SLinkedList()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print("The Slinkedlist before reversing it is :",end = " ")
obj.printList(obj.head)
obj.reverse_iter(obj.head)
print("\nThe Slinkedlist after reversing it is :",end = " ")
obj.printList(obj.head)
print("\nThe SlinkedinLIst after reversing to orginal using recursion is: ", end = "")
obj.head = obj.reverse_recer(obj.head)
obj.printList(obj.head)



