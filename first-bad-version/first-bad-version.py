# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

'''
1,2,3,4,5,6,7,8
'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        leftIdx = 0
        rightIdx = n
        
        while(leftIdx <= rightIdx):
            
            midIdx = (leftIdx + rightIdx)//2
            
            if isBadVersion(midIdx) == True:
                
                if midIdx == 0 or isBadVersion(midIdx-1) == False:
                    return midIdx
                
                elif isBadVersion(midIdx - 1) == True:
                    rightIdx = midIdx - 1
            
            if isBadVersion(midIdx) == False:
                leftIdx = midIdx + 1
            
        return -1
                    
            
        
        
        
        
        