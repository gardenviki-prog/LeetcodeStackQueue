class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        node = Node(x)
        node.next = self.head
        self.head = node

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        return data

    def top(self):
        return self.head.data

    def empty(self):
        return self.head is None

class FreqStack(object):

    def __init__(self):
        self.freq = {}    
        self.stacks = {}    
        self.max_f = 0

    def push(self, v):
        if v in self.freq:
            self.freq[v] += 1
        else:
            self.freq[v] = 1
        if self.freq[v] > self.max_f:
            self.max_f = self.freq[v]
        if self.freq[v] not in self.stacks:
            self.stacks[self.freq[v]] = Stack()
        self.stacks[self.freq[v]].push(v)

    def pop(self):
        v = self.stacks[self.max_f].pop()
        self.freq[v] -= 1
        if self.stacks[self.max_f].empty():
            self.max_f -= 1
        return v
