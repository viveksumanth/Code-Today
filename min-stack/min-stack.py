class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lis = []
        

    def push(self, val: int) -> None:
        self.lis.append(val)

    def pop(self) -> None:
        if len(self.lis) > 0:
            return self.lis.pop()
        return None

    def top(self) -> int:
        return self.lis[-1]

    def getMin(self) -> int:
        return min(self.lis)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()