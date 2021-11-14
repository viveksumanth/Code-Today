class Solution:
    def swap(self,nums,slow,fast):
        temp = nums[slow]
        nums[slow] = nums[fast]
        nums[fast] = temp
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums: return None
        i = len(nums)-1
        violated = 0
        
        while i >= 0:
            if nums[i-1] < nums[i]:
              violated = i-1
              break
            i-=1

        if i == 0:
            nums.reverse()
            return
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[violated]: 
                nums[i], nums[violated] = nums[violated], nums[i] 
                nums[violated+1:] = sorted(nums[violated+1:])
                return
        
        
            
            
            
            
            

        