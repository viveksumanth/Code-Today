class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        
        for i in range(0,len(matrix[0])):
            tempResult = []
            for j in range(0,len(matrix)):
                tempResult.append(matrix[j][i])
            result.append(tempResult)
            
        return result