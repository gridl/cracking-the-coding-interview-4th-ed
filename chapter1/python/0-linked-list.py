
# Linked List code

class Node:
    next = None
    data = None

    def __init__(self, data):
        self.data = data

    def appendToTail(self, val):
        end = Node(val)
        n = self
        while(n.next != None):
            n = n.next
        n.next = end

def delete_node(head, d):
    n = head

    if(n.data == d):
        return head.next

    while(n.next != None):
        if(n.next.data == d):
            n.next = n.next.next
            return head
        n = n.next

