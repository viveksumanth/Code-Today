class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        map = defaultdict(list)
        
        for each in intervals:
            start = each[0]
            map[start].append(each)
        
        sortedKeys = sorted(map.keys())

        sortedIntervals = []

        for eachKey in sortedKeys:
            startTimesSorted = map[eachKey]
            startTimesSorted.sort(reverse=True)
            sortedIntervals.extend(startTimesSorted)
            
        defStartTime = sortedIntervals[0][0]
        defEndTime = sortedIntervals[0][1]

        mergeIntervals = set()
        mergeIntervals.add((defStartTime, defEndTime))

        for each in range(1, len(sortedIntervals)):
            startTime, endTime = sortedIntervals[each]
            
            if defStartTime <= startTime and defEndTime >= endTime:
                continue

            mergeIntervals.add((startTime, endTime))
            defStartTime = startTime
            defEndTime = endTime

        return len(mergeIntervals)

