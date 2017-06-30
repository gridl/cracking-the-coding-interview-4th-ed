from linked_list import LinkedList, Node

def sum_lists(n1, n2, out):
    if not n1:
        return 0

    d1 = n1.data
    d2 = n2.data

    carry = sum_lists(n1.next, n2.next, out)

    s = d1 + d2 + carry
    ret = int(s/10)
    tot = s % 10

    node = Node(tot)
    node.next = out.head
    out.head = node

    return ret

def sum_lists_rev(n1,n2,out):
    carry = 0
    while n1:
        d1 = n1.data
        d2 = n2.data

        s = d1 + d2 + carry
        carry = int(s / 10)
        tot = s % 10

        print(tot)
        out.append(tot)

        n1 = n1.next
        n2 = n2.next


if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()

    l1.append(5)
    l1.append(1)
    l1.append(3)

    l2.append(2)
    l2.append(9)
    l2.append(5)

    print(l1)
    print(l2)

    out = LinkedList()
    sum_lists(l1.head, l2.head, out)
    print(out)


    l1 = LinkedList()
    l2 = LinkedList()

    l1.append(3)
    l1.append(1)
    l1.append(5)

    l2.append(5)
    l2.append(9)
    l2.append(2)

    out = LinkedList()
    sum_lists_rev(l1.head, l2.head, out)
    print(out)
