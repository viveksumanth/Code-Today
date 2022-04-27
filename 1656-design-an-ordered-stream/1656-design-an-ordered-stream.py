class OrderedStream:

    def __init__(self, n):
        self.n = n
        self.stream = [None]*n
        self.ptr = 0

    def insert(self, idKey, value):
        idKey -= 1
        
        self.stream[idKey] = value
        
        if self.ptr < idKey:
            return []
        
        while(self.ptr < self.n and self.stream[self.ptr] != None):
            self.ptr += 1
        
        return self.stream[idKey:self.ptr]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
