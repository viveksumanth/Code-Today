
class Solution:
    def maxSlidingWindow(self, nums, k):
        '''
        using monotonic decreasing queue and sliding window

        -> pop elements which are out of sliding window
        -> add elements into the deque and maintain monotonic decreasing property

        '''
    
        queue = collections.deque()
        maxArray = []
        pointerA = 0
        pointerB = 0

        for i in range(0,len(nums)):
            # print(queue)
            while(queue and queue[-1][0] < nums[i]):
                queue.pop()
            
            queue.append([nums[i],i])
            
            if pointerA > queue[0][1]:
                queue.popleft()
            
            if (i + 1) >= k:
                maxArray.append(queue[0][0])
                pointerA += 1  
        return(maxArray)


            
        