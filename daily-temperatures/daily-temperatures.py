class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
         0. 1. 2. 3. 4. 5. 6. 7
        [73,74,75,71,69,72,76,73]
                                        ans  = index - popped
      0  [0]
      1  [74]                [1]         ans =  1 - 0 = 1  ans[1] = 1
      2  [75]                [1,1]       ans =  2 - 1 = 1  ans[2] = 1
      3  [75,71,69]          [1,1]       ans =  3          ans[3] = 4
      4  [75,71]          []                               ans[4] = 5
      5. [75,72]                                           ans[]       
        '''
        nextDay = [0] * len(temperatures)
        stack = []
        for idx in range(0,len(temperatures)):
            
            while(stack and temperatures[stack[-1]] < temperatures[idx]):
                
                prevDay = stack.pop()
                nextDay[prevDay] = idx - prevDay
                
            stack.append(idx)
        return nextDay
            
        