import random
class Solution:

    def __init__(self, w: List[int]):
        
        self.w = w
        self.totalSum = 0
        self.prefixSum = []
        
        for idx in w:
            self.totalSum = self.totalSum + idx
            self.prefixSum.append(self.totalSum)


    def pickIndex(self) -> int:
        
        target = self.totalSum * random.random()
        
        low = 0
        high = len(self.prefixSum) - 1
        
        while(low <= high):
            
            mid = (low + high)//2
            
            if self.prefixSum[mid] < target:
                low = mid + 1 
            
            elif self.prefixSum[mid] > target:
                high = mid - 1
                
            else:
                return mid
            
        return low
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()