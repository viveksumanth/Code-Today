class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = float('-inf')
        for each in accounts:
            maxWealth = max(maxWealth,sum(each))
        
        return maxWealth
            
        