class Solution:
    
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def generate_states(current_state):
            states = []
            
            for i in range(4):
                
                current_state[i] = current_state[i] + 1
                if current_state[i] < 10:
                    new_state = current_state[:]
                    states.append(new_state)
                    
                elif current_state[i] > 10:
                    temp = current_state[:]
                    temp[i] = 0
                    new_state = temp[:]
                    states.append(new_state)
                current_state[i] = current_state[i] - 1
                
                current_state[i] = current_state[i] - 1
                if current_state[i] >= 0:
                    prev_state = current_state[:]
                    states.append(prev_state)
                    
                elif current_state[i] < 0:
                    temp = current_state[:]
                    temp[i] = 9
                    prev_state = temp[:]
                    states.append(prev_state)
                current_state[i] = current_state[i] + 1
                
            return states
                
                
        
        def bfs(state, target, deadends):
            queue = [state]
            steps = 0
            covered = set()
            s = [str(num) for num in state]
            check_state = ''.join(s)
            covered.add(check_state)
            # print(covered)
            while(len(queue)):

                for i in range(len(queue)):

                    node = queue.pop(0)
                    s = [ str(num) for num in node ]
                    check = ''.join(s)
                    
                    if check == target:
                        return steps
                    
                    states = generate_states(node)

                    for state in states:
                        
                        s = [str(num) for num in state]
                        check_state = ''.join(s)
                        
                        if check_state not in deadends and check_state not in covered :
                            covered.add(check_state)
                            queue.append(state)
                steps = steps + 1
                
            return -1
                        
                        
        
        def find_ways(deadends):
            start_state = [0,0,0,0]

            deadendsDict = dict()
            
            for i in deadends:
                deadendsDict[i] = 1
            s = [ str(num) for num in start_state ]
            check = ''.join(s)
            
            if check in deadendsDict:
                return -1
            
            return bfs(start_state, target, deadendsDict)
            
        return (find_ways(deadends))
            
            
        