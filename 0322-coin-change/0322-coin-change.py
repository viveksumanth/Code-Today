class Solution:

    def getPossibleCombinations(self,coins, amount, current):
        nextSum = []
        
        for eachCoin in coins:
            nextSumValue = eachCoin + current
            if nextSumValue <= amount:
                nextSum.append(nextSumValue)
                
        return nextSum
    
    def dfs(self, coins, amount, currentAmount, memo):
        if currentAmount in memo:
            return memo[currentAmount]
        if currentAmount == amount:
            return 0
        nextSum = self.getPossibleCombinations(coins, amount, currentAmount)
        minCount = float("inf")
        
        for each in nextSum:
            minCount = min(minCount, self.dfs(coins, amount, each, memo)+1)
        memo[currentAmount] = minCount 
        
        return minCount
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        currentAmount = 0
        coinsCount = 0
        memo = dict()
        self.dfs(coins, amount, currentAmount, memo)
        if memo[0] == float("inf"):
            return -1
        return memo[0]
        