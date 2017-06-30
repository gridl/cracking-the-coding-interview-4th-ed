from linked_list import LinkedList

class NthLinkedList(LinkedList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def nth_from_last(self, n):
        total_length = 0
        curr = self.head

        while curr:
            curr = curr.next
            total_length += 1

        curr = self.head
        l_last = total_length
        while curr:
            if l_last == n:
                return curr
            curr = curr.next
            l_last -= 1

        return None

    def nth_from_last2(self, n):
        front = self.head
        back = self.head
        distance = 0
        while distance != n and front:
            distance += 1
            front = front.next
        if distance < n: return None
        while front:
            front = front.next
            back = back.next

        return back


if __name__ == "__main__":
    nll = NthLinkedList()
    nll.append(1)
    nll.append(2)
    nll.append(3)
    nll.append(4)
    nll.append(5)
    nll.append(6)
    nll.append(7)

    print(nll)

    nth = nll.nth_from_last(3)
    print(nth.data)

    nth = nll.nth_from_last2(3)
    print(nth.data)



