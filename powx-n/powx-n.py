class Solution:

    def powerXN(self,power,value):

        if power == 0:
            return 1

        if value == 0:
            return 0

        if power == 1:
            return value

        answer = self.powerXN(power//2, value)

        if power%2 == 0:
            return answer*answer
        
        return answer*answer *value
            
        
    def myPow(self, x: float, n: int) -> float:
        
        '''
        divide and conquer
        '''
        if n < 0:
            x = 1/x
            n = -(n)
        return self.powerXN(n,x)
        
        