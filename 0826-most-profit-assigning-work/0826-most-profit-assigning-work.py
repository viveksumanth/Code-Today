class Solution:
    def getClosestJob(self, worker, difficulty, left, right):
        closest = left
        
        while(left <= right):
            mid = (left + right)//2
            
            if difficulty[mid] > worker:
                right = mid-1
            else:
                closest = difficulty[mid]
                left = mid+1
        
        return closest
                
        
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        '''
        d = [18,83,18]
        p = [54,98,19]
        w = [18,28,78]
        
        d:p = {
               18:54, 
               83:98, 
               18:19
               }
               
        d = [18, 18, 83]
        
        18 ->  closest - 18
        28 -> closest - 18
        18 -> closest - 18
        
        Think about the repeated difficulties and profits. 
        
        '''

        lookup = dict()
        lookup[0] = 0
        
        #Prepare Data
        for i in range(0,len(difficulty)):
            if difficulty[i] in lookup:
                lookup[difficulty[i]] = max(lookup[difficulty[i]], profit[i])
            else:
                lookup[difficulty[i]] = profit[i]

        maxValue = float("-inf")
        # sort for the binary search
        difficulty.sort()
        
        # setup the maximum profit for a job
        for each in difficulty:
            profitValue = lookup[each]
            maxValue = max(profitValue, maxValue)
            if maxValue > profitValue:
                lookup[each] = maxValue
        
        # get closest difficulty (maximum) for the worker's ability
        result = 0
        for eachWorker in worker:
            closestJob = self.getClosestJob(eachWorker, 
                                       difficulty, 
                                       left = 0, 
                                       right = len(difficulty)-1)
            result += lookup[closestJob]
            
        return result