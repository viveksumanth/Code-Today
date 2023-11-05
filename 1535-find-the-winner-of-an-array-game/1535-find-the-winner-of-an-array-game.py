class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        pointerA = 0
        pointerB = 1
        winCount = k
        prevElement = -1
        j = len(arr)
        
        while(winCount):
            if j == 0:
                return arr[0]
            
            if arr[pointerA] > arr[pointerB]:
                winElement = arr[pointerA]
                moveToEndElement = arr.pop(pointerB)
                arr.append(moveToEndElement)
                
            elif arr[pointerA] < arr[pointerB]:
                winElement = arr[pointerB]
                moveToEndElement = arr.pop(pointerA)
                arr.append(moveToEndElement)

            if prevElement == winElement:
                winCount -= 1
            else:
                winCount = k-1
                prevElement = winElement
                
            if winCount == 0:
                return winElement
            
            j = j - 1

            
        