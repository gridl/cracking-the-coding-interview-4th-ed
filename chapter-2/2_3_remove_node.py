from linked_list import LinkedList

def remove_node(n):
    n.data = n.next.data
    n.next = n.next.next

if __name__ == "__main__":
    ll = LinkedList(with_data=True)
    print(ll)
    n2 = ll.get(2)
    remove_node(n2)
    print(ll)
