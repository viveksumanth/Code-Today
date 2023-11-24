class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        result = 0
        j = 1
        piles.sort(reverse = True)
        
        l,r = 1,len(piles)
        
        while(l<r):
            result = result + piles[l]
            l = l + 2
            r = r - 1
            
        return result