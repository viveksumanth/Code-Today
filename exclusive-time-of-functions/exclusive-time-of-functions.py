class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        prevTimeStamp = 0
        ans = [0]*n
        stack = []
        # fn, typ, time = log.split(':')
        for eachLog in logs:
            
            func, operation, time = eachLog.split(':')
            time = int(time)
            func = int(func)
            
            
            if operation == 'start':
                
                if stack:
                    ans[stack[-1]] +=  time - prevTimeStamp
                    
                stack.append(func)
                prevTimeStamp = time
            
            elif operation == 'end':
                ans[stack.pop()] += time - prevTimeStamp + 1
                
                prevTimeStamp = time + 1
                

            
        return ans
