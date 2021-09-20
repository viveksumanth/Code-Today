class Solution:
    
#     def coinchange(self,coins,amount,count,countarr):
        
        
#         if amount == 0:
#             countarr.append(count)
#             return countarr
        
#         if amount < 0:
#             return -1
        
#         for i in coins:
            
#             if amount - i >= 0:
            
#                 self.coinchange(coins,amount-i,count+1,countarr)
            
        # return countarr



    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        arr = [amount+1] * (amount+1)
        arr[0] = 0
        
        for i in coins:
            for j in range(i,len(arr)):
                
                arr[j] =  min(arr[j - i] + 1, arr[j])
        
        if arr[amount] <= amount:
            return arr[amount]
        return -1
        
#         countarr = (self.coinchange(coins,amount,0,[]))
        
#         print(countarr)
#         if len(countarr) > 0:
#             return(min(countarr))
        
#         return -1
        
        
        
        
        
        
        