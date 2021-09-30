# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def binarysearch(l,r):
            
            m = (l + r)//2
            # print(l,r,m,isBadVersion(m))
            
            if r >= l:
                
                if isBadVersion(m) == True and isBadVersion(m-1) == True:

                    return binarysearch(l,m)
                
                elif isBadVersion(m) == False:
                    return binarysearch(m+1,r)
                    
                elif isBadVersion(m) == True and isBadVersion(m-1) == False:
                    return m
                
            return -1
        
        return binarysearch(1,n)
        
        
        