class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        [10]
        
        
        [-2,-1,1,2]
        
        [-2,-1,1,2,-5 ]
        
        -ve and + ve sequence accepted,
        but 
        +ve and -ve is not accepted. 
        
        [-2,-1,-5]  -> while stack[-1] is positive and greater than current then pop and append
        
        [-2,-1,5,2,-5] -> while stack[-1] is positive and equal then pop and contine, dont append
        
        [2,-1,5,2,-1] -> while stack[-1] is postive and if current is less that stack[-1], dont pop and contine dont append  
        '''
        stack = []
        
        for eachElement in asteroids:
            if len(stack) == 0:
                stack.append(eachElement)

            elif stack[-1] < 0: #[-1,-1,-3]
                stack.append(eachElement)
            elif stack[-1] > 0: #[5,1,-3]
                if eachElement > 0:
                    stack.append(eachElement)
                else:
                    while(stack and stack[-1] > 0 and stack[-1] < abs(eachElement)):
                        stack.pop()
                    
                    if stack and stack[-1] == abs(eachElement):
                        stack.pop()
                        continue
                    if stack and stack[-1] > 0 and eachElement < stack[-1]:
                        continue
                    
                    stack.append(eachElement)
        return stack
        