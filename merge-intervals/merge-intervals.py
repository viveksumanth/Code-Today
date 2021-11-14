
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort()
        allIntervals = []

        for idx in range(0, len(intervals)):
            if len(allIntervals) == 0:
                allIntervals.append(intervals[idx])

            else:
                if allIntervals[-1][1] >= intervals[idx][0]:
                    allIntervals[-1][1] = max(allIntervals[-1][1], intervals[idx][1])
                else:
                    allIntervals.append(intervals[idx])

        return allIntervals
