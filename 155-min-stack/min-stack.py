class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        self.minVal=float("inf")

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.minVal>=val:
            self.minStack.append(self.minVal)
            self.minVal=val

    def pop(self):
        """
        :rtype: None
        """
        curr = self.stack.pop()
        if curr == self.minVal:
            self.minVal=self.minStack.pop()


            

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()