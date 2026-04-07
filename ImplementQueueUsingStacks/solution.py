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


class MyQueue:

    def __init__(self):
        self.main_s = Stack()
        self.help_s = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while not self.main_s.empty():
            self.help_s.push(self.main_s.pop())
        self.main_s.push(x)
        while not self.help_s.empty():
            self.main_s.push(self.help_s.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.main_s.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.main_s.top()

    def empty(self):
        """
        :rtype: bool
        """
        return self.main_s.empty()
