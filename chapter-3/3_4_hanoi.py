from stack import Stack


def move_towers(amount, beg, aux, end):

    if amount == 1:
        end.push(beg.pop())
        return

    move_towers(amount - 1, beg, end, aux)
    move_towers(1, beg, aux, end)
    move_towers(amount - 1, aux, beg, end)

if __name__ == "__main__":
    beg = Stack()
    aux = Stack()
    end = Stack()

    beg.push(4)
    beg.push(3)
    beg.push(2)
    beg.push(1)

    print(beg)
    print(aux)
    print(end)

    move_towers(4, beg, aux, end)
    print(beg)
    print(aux)
    print(end)
