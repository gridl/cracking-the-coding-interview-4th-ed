
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return "Data %s: Next -> %s" % (self.data, self.next)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node()
        node.data = data
        node.next = None

        if self.head == None:
            self.head = node

        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = node

    def remove(self, data):
        node = self.head
        if node.data == data:
            self.head = self.head.next
        else:
            while node.next:
                if node.next.data == data:
                    node.next = node.next.next
                    break

        return node


    def printList(self):
        print(self.head)

class Stack:
    def __init__(self):
        self.top = None

    def pop(self):

        if self.top != None:
            item = self.top.data
            self.top = self.top.next
            return item

        return None

    def push(item):
        def __init__(self):
            self.first = None
            self.last = None

        def enqueue(self, data):
            if not self.first:
                self.last = Node(data)
                self.first = self.last
            else:
                self.last.next = Node(data)
                self.last = self.last.next

        def deqeue(self, n):
            if self.first != None:
                data = self.first.data
                self.first = self.first.next
                return data
            return None




