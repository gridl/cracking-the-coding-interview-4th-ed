from linked_list import LinkedList

class CircularLinkedList(LinkedList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def circular_node(self):
        curr = self.head
        elems = set()
        while curr:
            if curr in elems:
                return curr
            elems.add(curr)
            curr = curr.next

if __name__ == "__main__":
    ll = CircularLinkedList(with_data=True)
    n3 = ll.get(3)
    last = ll.get(7)
    last.next = n3
    circ = ll.circular_node()
    print(circ)
