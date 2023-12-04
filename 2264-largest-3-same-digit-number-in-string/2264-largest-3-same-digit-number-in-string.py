class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        pointerA = 0
        prevValue = "-1"
        counter = 0
        
        for i in range(0,len(num)):
            if num[pointerA] == num[i]:
                counter += 1
            else:
                if counter >= 3:
                    if int(prevValue) < int(num[pointerA]):
                        prevValue = num[pointerA]
                    
                counter = 1 
                pointerA = i
        
        if counter >= 3:
            if int(prevValue) < int(num[pointerA]):
                prevValue = num[pointerA]
        
        if prevValue == "-1":
            return ""
        
        return prevValue*3
            

        

            
        