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
    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        print(slow.val)

         

    
obj = SLinkedList()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print("The Slinkedlist before reversing it is :",end = " ")
obj.printList(obj.head)
print("\nThe middle element in the ll is : ",end = "")
obj.middle()



