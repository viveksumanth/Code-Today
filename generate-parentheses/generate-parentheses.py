class Solution:
    def generator(self, nOpen, nClose, n , cs, solutions):
        # print(''.join(cs))
        
        if nClose == n:
            solutions.append(''.join(cs[:]))
            return
        
        if nOpen < n:
            cs.append('(')
            self.generator(nOpen+1,nClose, n ,cs, solutions)
            cs.pop()
        
        if nClose < nOpen:
            cs.append(')')
            self.generator(nOpen,nClose+1,n,cs,solutions)
            cs.pop()

        return solutions
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        nOpen = 0
        nClose = 0
        
        solutions = self.generator(nOpen, nClose, n,[],[])
        
        return solutions
        
        
        