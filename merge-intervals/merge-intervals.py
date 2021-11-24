
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        mergeIntervals = []

        intervals.sort()  #[1,5][1,4]


        for currentInterval in intervals:



            if len(mergeIntervals) and mergeIntervals[-1][1] >= currentInterval[0]:


                mergeIntervals[-1][1] = max(mergeIntervals[-1][1], currentInterval[1])

            else:

                mergeIntervals.append(currentInterval)


        return mergeIntervals
