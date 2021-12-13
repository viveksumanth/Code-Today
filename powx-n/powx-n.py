class Solution:
    def myPow(self, x: float, n: int, result = 1) -> float:
        
        '''
        
        x^n = x * x ... n
        
         10
         
        
        '''
        if n < 0:
            x = 1/x
            n = -(n)
            
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        result = self.myPow(x,n//2)
        
        if n % 2 == 0:
            result = result * result
        else:
            result = result * result * x
        
        return result
        
        
        