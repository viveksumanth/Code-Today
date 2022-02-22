class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            
            if count == 0:
                candidate = num
            if num == candidate:
                count = count + 1
            else:
                count -= 1

        return candidate