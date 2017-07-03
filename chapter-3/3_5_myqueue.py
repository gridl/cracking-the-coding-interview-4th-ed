from stack import Stack

class MyQueue:
    def __init__(self):
        self._front = Stack()
        self._back = Stack()

    def push(self, data):
        return self._front.push(data)

    def pop(self):
        node = None
        if len(self._back):
            node = self._back.pop()
        elif len(self._front):
            while self._front.peek():
                self._back.push(self._front.pop())
            node = self._back.pop()

        return node

    def __str__(self):
        return "Front: " + str(self._front) + "\nBack: " + str(self._back)


if __name__ == "__main__":

    m = MyQueue()

    m.push(1)
    print(m)

    m.push(2)
    print(m)

    m.push(3)
    print(m)

    m.pop()
    print(m)

    m.pop()
    print(m)

    m.pop()
    print(m)


