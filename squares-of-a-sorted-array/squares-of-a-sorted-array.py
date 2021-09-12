class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        w = [-1]*(len(nums))
        wp = len(nums)-1
        lp = 0
        rp =len(nums)-1
        
        while(lp <= rp):
            if nums[lp] * nums[lp] > nums[rp] * nums[rp]:
                w[wp] = nums[lp] * nums[lp]
                wp = wp - 1
                lp = lp + 1
            else:
                w[wp] = nums[rp] * nums[rp]
                rp = rp - 1
                wp = wp - 1
        
        return w