from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        direction = True  #up
        diagonalSum = defaultdict(list)
        result = []

        for row in range(0,len(matrix)):
            for col in range(0,len(matrix[0])):
                diagonalSum[row+col].append(matrix[row][col])

        for row in diagonalSum:
            if direction == True:

                result += diagonalSum[row][::-1]
                direction = not direction
            else:
                result += diagonalSum[row]
                direction = not direction

        return result
    