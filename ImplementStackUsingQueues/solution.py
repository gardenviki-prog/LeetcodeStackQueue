class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x):
        node = Node(x)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def front(self):
        return self.head.data

    def empty(self):
        return self.head is None
        

class MyStack:

    def __init__(self):
        self.main_q = Queue()
        self.help_q = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.help_q.push(x)
        while not self.main_q.empty():
            self.help_q.push(self.main_q.pop())
        temp = self.main_q
        self.main_q = self.help_q
        self.help_q = temp

    def pop(self):
        """
        :rtype: int
        """
        return self.main_q.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.main_q.front()

    def empty(self):
        """
        :rtype: bool
        """
        return self.main_q.empty()
