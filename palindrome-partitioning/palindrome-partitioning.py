class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def parlindrome_part(s,start, ps, solution):
            
            if start == len(s):
                solution.append(ps[:])
                return
            
            for i in range(start+1,len(s)+1):
                current = s[start:i]

                if current == current[::-1]:
                    parlindrome_part(s,i,ps+[current],solution)

                
            return solution
        
        return parlindrome_part(s,0,[],[])
    
        