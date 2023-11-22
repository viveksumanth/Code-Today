from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        resultMap = defaultdict(list)

        for rowIdx in range(0, len(nums)):
            for colIdx in range(0, len(nums[rowIdx])):
                currentDiagonal = rowIdx+colIdx
                resultMap[currentDiagonal].append(nums[rowIdx][colIdx])
        
        result = []
        for eachDiag in resultMap:
            curDiag = resultMap[eachDiag]
            result.extend(curDiag[::-1]) 
        return result