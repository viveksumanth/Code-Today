
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        pointerB = 0
        stack = []
        maxmArray = []
        
        # k == 1 which means that at the window of size 1 k should be 1
        if k == 1:
            return nums
        
        for pointerA in range(0,len(nums)):
            
            # maintaing window of size k
            while(k == 0):
                maxmArray.append(nums[stack[0]])
                pointerB = pointerB + 1
                k += 1
            
            # maintaing monotonocity
            while(stack and nums[stack[-1]] < nums[pointerA]):
                stack.pop()
            
            # removing the element which is out of bound 
            if stack and stack[0] < pointerB:
                    stack.pop(0)
            
            # adding new element
            stack.append(pointerA)
            k = k - 1
            
        # for the last window
        maxmArray.append(nums[stack[0]])
        return maxmArray

            
        