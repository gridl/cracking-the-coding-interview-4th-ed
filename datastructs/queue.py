from linked_list import LinkedList, Node

class Queue(LinkedList):
    def __init__(self, *args, **kwargs):
        if "with_data" in kwargs:
            print("with_data not supported")
            kwargs.pop("with_data")

        super().__init__(*args, **kwargs)
        self.tail= None

    def append(self, data):
        self.enqueue(data)

    def enqueue(self, data):

        node = Node(data)

        if not self._head:
            self._head = node
            self.tail = self._head
        else:
            self._head.next = node
            self._head = self._head.next

        self._size += 1

        return node

    def dequeue(self):
        if not self._head:
            return None

        end = self.tail
        self.tail = self.tail.next
        self._size -= 1
        return end

    def __str__(self):
        ret = []
        ret.append("Nodes:")
        curr = self.tail
        while curr:
            ret.append(str(curr))
            curr = curr.next
        return " -> ".join(ret)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q)

    q.enqueue(8)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
