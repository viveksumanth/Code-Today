class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        # print(self.stack)

    def pop(self) -> int:
        if len(self.stack) == 0:
            # print(self.stack)
            return -1
        else:
            # print(self.stack)
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for eachIdx in range(0,k):
            if eachIdx < len(self.stack):
                self.stack[eachIdx] += val
        # print(self.stack)
        

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)