# Describe how you could use a single array to implement three stacks.

# What will the stacks themselves store?
#   Numbers
# Is there a limit on the number of elements?
#   No
# Should it grow dynamically?
#   Not initially
# Just to confirm, is this an array or a linkedlist?
#   This is an array

# Ok so I would take an array, and initialize the length itself to be a solid length
# And then I would divide the length of the array on 3, keeping track of the start and head
# of each of these stacks. Then I would push each of the elements
# If I need to grow the array dynamically I would just do so as soon as I run out of space

class ArrayStack:

    def __init__(self, num_stacks=3):

        length = 2*num_stacks

        if num_stacks <= 0:
            raise Exception("length needs to be larger than twice the number of stacks")

        self._array = [0] * length
        self._length = length
        self._num_stacks = num_stacks
        self._heads = []

        for i in range(num_stacks):
            self._heads.append(int(self._length * i / num_stacks))

    def _increase_size(self):
        print("resizig.....")
        new_len = self._length * 2
        new_array = [0] * new_len
        new_heads = []

        for i in range(self._num_stacks):
            to_idx = self._heads[i]
            from_idx = int(self._length * i / self._num_stacks)
            new_from_idx = int(new_len * i / self._num_stacks)
            new_to_idx = new_from_idx + (to_idx - from_idx)
            new_array[new_from_idx:new_to_idx] = self._array[from_idx:to_idx]
            new_heads.append(new_to_idx)

        self._array = new_array
        self._length = new_len
        self._heads = new_heads

    def push(self, stack, data):

        if stack >= self._num_stacks or stack < 0:
            return False

        head = self._heads[stack]

        if head >= int(self._length * (stack + 1) / self._num_stacks):
            self._increase_size()
            head = self._heads[stack]

        self._array[head] = data
        self._heads[stack] += 1


    def pop(self, stack):
        if stack >= self._num_stacks or stack < 0:
            return None

        head = self._heads[stack]
        if head < int(self._length * stack / self._num_stacks):
            return None

        data = self._array[head-1]
        self._heads[stack] -= 1

    def __str__(self):
        ret = []
        for i in range(len(self._heads)):
            ret.append("Stack #" + str(i) + ": ")
            head = self._heads[i]
            j = int(self._length * i / self._num_stacks)
            while j < head:
                ret.append(str(self._array[j]) + " " )
                j += 1

            ret.append("\n")

        return "".join(ret)



if __name__ == "__main__":

    a = ArrayStack()
    a.push(0,1)
    a.push(0,2)
    a.push(0,3)
    a.push(0,4)
    a.push(0,4)
    a.push(0,4)
    print(a)

    a.push(1,0)
    a.push(1,1)
    a.push(1,2)
    print(a)

    a.push(2,3)
    a.push(2,4)
    a.push(2,5)
    a.push(2,3)
    a.push(2,4)
    a.push(2,5)
    print(a)
    a.push(2,3)
    print(a)
    a.push(2,4)
    print(a)
    a.push(2,5)
    print(a)
    a.push(2,3)
    a.push(2,4)
    a.push(2,5)
    print(a)

    a.pop(0)
    a.pop(1)
    a.pop(2)
    print(a)

    a.pop(0)
    a.pop(1)
    a.pop(2)
    print(a)

    a.pop(0)
    a.pop(1)
    a.pop(2)
    print(a)


