from stack import Stack

def sorted_stack(s):
    r = Stack()
    while s._size:
        tmp = s.pop().data
        while len(r) and r.peek() > tmp:
                s.push(r.pop().data)
        r.push(tmp)
    return r


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(4)
    s.push(2)
    s.push(3)

    print(s)

    r = sorted_stack(s)

    print(r)



