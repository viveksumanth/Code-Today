class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = []

        while(n > 1):
            newNum = n%10
            if newNum != 0:
                nums.append(newNum)
            n = n//10
        nums.append(n)

        numsSum = sum(nums)

        mul = 1

        totalSum = 0
        for each in nums:
            totalSum += each*mul
            mul *= 10
        
        return totalSum * numsSum
            
        