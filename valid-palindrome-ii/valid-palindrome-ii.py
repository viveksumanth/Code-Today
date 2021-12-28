class Solution:
    def __init__(self):
        self.tolerate = 0
        
    def validPalindromeHelper(self,s,pointerA,pointerB):
        
        while(pointerA < pointerB):

            if s[pointerA] == s[pointerB]:
                pointerA += 1
                pointerB -= 1
                
            else:
                one = s[pointerA:pointerB]
                two =  s[pointerA + 1:pointerB + 1]

                if one == one[::-1] or two == two[::-1]:
                    return True
                else:
                    return False
            
        return True
                
                
    def validPalindrome(self, s: str) -> bool:
        
        '''
        
        can tolerate atmost one character
        
        |
        a b c
            |       [a b] [b c]
            
        one = s[pointerA:pointerB]
        two =  s[pointerA + 1:pointerB + 1]
        
          |
        a b b c a
              |
        
        b b 
        
        b c
        
        '''
        s = list(s)
        pointerA = 0
        pointerB = len(s) - 1
        return self.validPalindromeHelper(s,pointerA,pointerB)