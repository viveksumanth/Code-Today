import numpy
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        
        arr = [[0]*(amount+1)]*(len(coins)+1)
        # print(arr)
        for each in range(len(arr)):
            arr[each][0] = 1
        # print(arr)
        
        for i in range(1,len(arr)):
            currcoin = coins[i-1]
            for j in range(coins[i-1],len(arr[0])):
                arr[i][j] = arr[i][j-currcoin] + arr[i-1][j]
        
        # print(arr)
        return (arr[-1][-1])
        
        