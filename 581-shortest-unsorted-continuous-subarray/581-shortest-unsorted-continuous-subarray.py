class Solution:
    def findUnsortedSubarray(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        find the minimum of the inflation point and maximum in the 
        inflation point

        * come from forward and find the first element which decreases
        firstDecreasing = 7
                             |
        [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

        * Come from back and find the first element which increases
        firstIncreasing = 12

        now find the place for the firstDecresing and make it left range
        and find the place for the first Increasing element coming from a

        [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]
        '''
        firstDecreasingNumber = float('-inf')
        leftRange = 0
        rightRange = 0
        decrementFlag = False
        incrementFlag = False
        firstIncreasingNumber = float('inf')

        for eachIdx in range(1,len(array)):

            if decrementFlag == False:
                if array[eachIdx-1] <= array[eachIdx]:
                    continue
                else:
                    decrementFlag = True
                    firstDecreasingNumber = array[eachIdx]
            else:
                firstDecreasingNumber = min(firstDecreasingNumber, array[eachIdx])


        for eachIdx in range(len(array)-1,0,-1):

            if incrementFlag == False:
                if array[eachIdx-1] <= array[eachIdx]:
                    continue
                else:
                    incrementFlag = True
                    firstIncreasingNumber = array[eachIdx-1]
            else:
                # print(array[eachIdx-1], array[eachIdx],firstIncreasingNumber)
                firstIncreasingNumber = max(firstIncreasingNumber,array[eachIdx-1])

        # print(firstIncreasingNumber,firstDecreasingNumber)

        if firstIncreasingNumber== float('inf') and firstDecreasingNumber == float('-inf'):
            return 0

        for eachIdx in range(0,len(array)):

            if firstDecreasingNumber < array[eachIdx]:
                leftRange = eachIdx
                break

        for eachIdx in range(len(array)-1,-1,-1):

            if firstIncreasingNumber > array[eachIdx]:
                rightRange = eachIdx
                break

        return rightRange - leftRange + 1
