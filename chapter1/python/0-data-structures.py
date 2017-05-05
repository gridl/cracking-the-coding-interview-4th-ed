
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return "Data %s: Next -> %s" % (self.data, self.next)

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.curNode = self.head

    def insertNode(self, data):
        node = Node()
        node.data = data
        node.next = None

        if self.head.data == None:
            self.head = node
            self.curNode = node

        else:
            self.curNode.next = node
            self.curNode = node

    def printList(self):
        print(self.head)

class Stack:
    def __init__(self):
        self.top = None

    def pop(self):

        if self.top != None:
            item = top.data
            self.top = self.top.next
            return item

        return None

    def push(item):
        def __init__(self):
            self.first = None
            self.last = None

        def enqueue(data):
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




