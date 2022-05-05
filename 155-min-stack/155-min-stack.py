class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lis = []
        self.min = float('inf')

    def push(self, val: int) -> None:

        if len(self.lis) == 0:
            self.lis.append([val,val])
            return
        
        currentMin = self.lis[-1][1]
        currentMin = min(currentMin,val)
        self.lis.append([val,currentMin])

    def pop(self) -> None:

        if len(self.lis) > 0:
            return self.lis.pop()
        return None

    def top(self) -> int:

        return self.lis[-1][0]

    def getMin(self) -> int:

        return self.lis[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()