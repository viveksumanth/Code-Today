class Solution:
    def countBits(self, n: int) -> List[int]:
        
        newArray = [0,1]
        
        current = 2
        numberOfOnes = 0
        
        if current > n:
            return newArray[:n+1]
        
        while(current <= n):
            
            newElement = current
    
            currentOnes = newArray[newElement//2] + newElement%2
            
            newArray.append(currentOnes)
            
            current+=1
        
        return newArray[:n+1]
    
        
        
        