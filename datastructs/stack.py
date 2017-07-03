from linked_list import LinkedList, Node

class Stack(LinkedList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def push(self, data):
        node = Node(data)
        if not self._head:
            self._head = node
        else:
            node.next = self._head
            self._head = node

        self._size += 1

    def pop(self):
        if not self._head:
            return None
        top = self._head
        self._head = self._head.next
        self._size -= 1
        return top

    def peek(self):
        return self._head.data if self._head else None

if __name__ == "__main__":
    s = Stack(with_data=True)
    print(s)

    s.push(-1)
    print(s)

    print(s.pop())
    print(s)
    print(s.pop())
    print(s)
    print(s.pop())
    print(s)

