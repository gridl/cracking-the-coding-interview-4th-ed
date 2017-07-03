from stack import Stack
import sys

class MinStack(Stack):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._min = Stack()

    def push(self, data):
        curr_min = self._min.peek()

        if not curr_min or data <= curr_min:
            self._min.push(data)

        super().push(data)

    def pop(self):
        node = super().pop()
        if node:
            if node.data == self._min.peek():
                self._min.pop()
        return node

    def min(self):
        return self._min.peek()

if __name__ == "__main__":
    m = MinStack()
    m.push(5)
    m.push(4)
    m.push(3)
    m.push(3)
    m.push(3)
    m.push(2)
    m.push(1)
    print(m.min())

    m.pop()
    print(m.min())

    m.pop()
    print(m.min())
    m.pop()
    print(m.min())
    m.pop()
    print(m.min())
    m.pop()
    print(m.min())
    m.pop()
    print(m.min())


