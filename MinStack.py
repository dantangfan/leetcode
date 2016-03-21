class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.size and self.stack[self.min] > x:
            self.min = self.size
        self.size += 1
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.size -= 1
        self.stack.pop()
        if self.min == self.size and self.stack:
            self.min = 0
            for i, v in enumerate(self.stack):
                if v < self.stack[self.min]:
                    self.min = i

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.min]

s = MinStack()
s.push(-3)
s.push(-4)
s.push(-5)
print s.top()
s.pop()
print s.getMin()