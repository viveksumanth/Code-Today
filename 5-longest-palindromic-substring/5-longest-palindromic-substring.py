class Solution:
    
    def checkParlindrome(self,s,left,right,currentLength):

        leftRange,rigthRange = [left,right]
        
        while(left >= 0 and right <= len(s) - 1 ):
            
            if s[left] == s[right]:
                currentLength += 2
                left = left - 1
                right = right + 1
            else:
                break
        
        return [left+1,right-1]
                
    
    def longestPalindrome(self, s: str) -> str:
        
        '''
        generate all the perumatations of the string 
        
        
        and find the longest permutation.
        
           |        
        [b a b a d]
         |
        
        '''
        if len(s) == 1:
            return s
        
        if len(s) == 0:
            return ''

        length = 1
        longest = ''
        
        for eachIdx in range(1,len(s)):
            
            currentEven = self.checkParlindrome(s,eachIdx-1,eachIdx,2)
            
            left,right = currentEven
            
            if right - left + 1 >= length:
                longest = s[left:right+1]
                length = right - left + 1
            
            currentOdd = self.checkParlindrome(s,eachIdx-1,eachIdx+1,1)

            left,right = currentOdd
            
            if right - left + 1 >= length:
                longest = s[left:right+1]
                length = right - left + 1
                
        return longest
    
    
            
            
            
        