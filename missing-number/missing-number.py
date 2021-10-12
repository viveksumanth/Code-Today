class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_of_nums = sum(nums)
        size = len(nums)
        return ((size*(size+1))//2) - sum_of_nums