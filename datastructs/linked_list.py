
class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, with_data=False):
        self._head = None
        self._size = 0

        if with_data:
            self.append(0)
            self.append(1)
            self.append(2)
            self.append(3)
            self.append(4)
            self.append(5)
            self.append(6)
            self.append(7)

    def append(self, data):
        node = Node(data)

        if not self._head:
            self._head = node
            return node

        else:
            current = self._head
            while current.next:
                current = current.next

            current.next = node

        self._size += 1

        return node

    def get(self, index):
        curr = self._head
        curr_idx = 0
        while curr:
            if curr_idx == index:
                return curr
            curr_idx += 1
            curr = curr.next

    def __len__(self):
        return self._size

    def __str__(self):
        return_str = []
        node = self._head
        return_str = ["Nodes: "]
        while node:
            return_str.append(str(node.data))
            node = node.next

        return " -> ".join(return_str)

if __name__ == "__main__":
    ll = LinkedList(with_data=True)
    print(ll)

    n2 = ll.get(2)
    print(n2)

