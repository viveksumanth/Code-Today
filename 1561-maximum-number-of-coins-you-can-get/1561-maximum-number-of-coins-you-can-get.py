class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        right = len(piles)-1
        maxCoins = 0
        while(left <= right):
            maxCoins += piles[right-1]
            left += 1
            right -= 2
        
        return maxCoins