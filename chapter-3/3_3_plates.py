from stack import Stack

class SetOfStacks:
    def __init__(self, max_size=5):
        self._max_size = max_size
        self._stacks = []
        self._stacks.append(Stack())
        self._size = 0

    def push(self, data):
        curr_stack = self._stacks[-1]
        curr_size = len(curr_stack)

        if curr_size >= self._max_size:
            self._stacks.append(Stack())
            curr_stack = self._stacks[-1]

        node = curr_stack.push(data)
        self._size += 1
        return node

    def pop(self):
        curr_stack = self._stacks[-1]
        if len(self._stacks) == 1:
            return curr_stack.pop()

        node = curr_stack.pop()
        if not len(curr_stack):
            self._stacks.pop()

        return node

    def popAt(self, idx):
        stack_idx = int(idx / self._max_size)
        actual_idx = idx % self._max_size
        stack = self._stacks[stack_idx]
        node = stack.popAt(actual_idx)
        # Now we need to shift everything
        curr_idx = stack_idx
        next_stack = None

        while curr_idx < len(self._stacks) - 1:
            curr_stack = self._stacks[curr_idx]
            next_stack = self._stacks[curr_idx + 1]
            curr_stack.push(next_stack.popAt(0))
            curr_idx += 1

        if not len(next_stack):
            self._stacks.pop()

        return node

    def __str__(self):
        return "\n".join([str(s) for s in self._stacks])


if __name__ == "__main__":

    s = SetOfStacks()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)
    s.push(11)
    s.push(12)
    s.push(13)
    s.push(14)
    s.push(15)
    print(s)

    print("\nthat's done\n")

    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print(s)

    print("\nthat's done\n")
    s.popAt(0)
    print(s)

    print("\nthat's done\n")
    s.popAt(0)
    print(s)

    s.push(8)
    print(s)

    print("\nthat's done\n")
    s.popAt(4)
    print(s)







