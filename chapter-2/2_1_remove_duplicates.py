from linked_list import LinkedList

class ExtLinkedList(LinkedList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def remove_dup(self):
        curr = self.head
        if not (curr and curr.next): return

        prev = None
        elems = set()

        while curr:
            if curr.data in elems:
                prev.next = curr.next
            else:
                elems.add(curr.data)
                prev = curr

            curr = curr.next

    def remove_dup_no_mem(self):
        i = self.head
        while i and i.next:
            j = i.next
            p = i
            while j:
                if i.data == j.data:
                    p.next = j.next
                else:
                    p = j
                j = j.next
            i = i.next

if __name__ == "__main__":
    ell = ExtLinkedList()
    ell.append("hi")
    ell.append("hello")
    ell.append("hi")
    print(ell)
    ell.remove_dup()
    print(ell)

    ell.append("hi")
    ell.append("hello")
    ell.append("hi")
    print(ell)
    ell.remove_dup_no_mem()
    print(ell)


