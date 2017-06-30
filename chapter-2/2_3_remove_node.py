from linked_list import LinkedList

def remove_node(n):
    n.data = n.next.data
    n.next = n.next.next


