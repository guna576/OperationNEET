class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        new_head = head.next
        current = head
        while current:
            temp = current.next
            current.next = temp.next
            current = current.next
            if temp.next:
                temp.next = temp.next.next
        
        return new_head
    
# You can do it using Hashmap like <Original Node: Copied Node>
# Put all nodes in this order and put connections as well and return HashMap[original Head]


# Doing without map is by adding nodes one after original node. alternate
# Then putting same connection like original and removing with original nodes and making original perfect
# return dummy.next as it was pointing to the new copied nodes 

# unrealistic to come up without remembering the concept
