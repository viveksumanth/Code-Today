class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i]*(-1)
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)
    
        
        return heapq.heappop(nums)*(-1)
        