class Solution:
    def maximumSwap(self, num: int) -> int:

        swapIndex = None
        number = -1
        nums = [int(x) for x in str(num)] 

        for idx in range(1,len(nums)):
            if nums[idx-1] < nums[idx]:

                number = max(number, nums[idx]) 

                if swapIndex == None:
                    swapIndex = idx

                if nums[swapIndex] != number: 
                    swapIndex = idx
            
            if number == nums[idx]:
                swapIndex = idx
                

        if swapIndex != -1 and number != -1:
            for cIdx in range(0,len(nums)):

                if nums[cIdx] < number:
                    nums[cIdx], nums[swapIndex] = nums[swapIndex], nums[cIdx]
                    break
        

        nums = [str(i) for i in nums]
        
        return int(''.join(nums))