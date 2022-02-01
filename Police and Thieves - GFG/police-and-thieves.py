#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3
import heapq

class Solution:
    def catchThieves(self, arr, n, k): 
        police = []
        theif = []
        count = 0
        p = 0 
        t = 0
        for eachCharIdx in range(n):
            eachChar = arr[eachCharIdx]
            
            if eachChar == 'P':
                police.append(eachCharIdx)
            
            elif eachChar == 'T':
                theif.append(eachCharIdx)
        
        while(p <= len(police) - 1 and t <= len(theif)-1):
            
            if abs(police[p] - theif[t]) <= k:
                count = count + 1
                p = p + 1
                t = t + 1
            
            elif police[p] > theif[t]:
                t = t + 1
            
            else:
                p = p + 1
        
        return count
                
                
                
                
                
        
        # code here 

#{ 
#Driver Code Starts.

if __name__=='__main__': 
	t = int(input())
	for _ in range(t):
		line1 = list(map(int, input().strip().split()))
		n = line1[0]
		k = line1[1]
		arr = list(input().strip().split())
		obj = Solution()
		print(obj.catchThieves(arr, n, k))


#} Driver Code Ends