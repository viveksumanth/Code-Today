class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        ans = float('inf')
        n = len(nums)
        while(low <= high):
            
            mid = low + (high-low)//2

            if nums[mid] <= nums[n-1]:
                ans = nums[mid]
                
                high = mid - 1
            
            else:
                low = mid + 1
        
        return ans
    
                