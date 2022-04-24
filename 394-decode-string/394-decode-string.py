class Solution:
    def decodeString(self, s: str) -> str:
        #add elements in the stack untill the ']' is hit
        stack = []
        
        for each in s:
            
            if each != ']':
                stack.append(each)
            
            else:

                sentence = []
                number_of_times = []
                while(stack[-1] != '['):
                    char = stack.pop()
                    sentence.append(char)
                
                stack.pop()
                
                while(stack and stack[-1].isdigit()):
                    number = stack.pop()
                    number_of_times.append(number)
                
                number_of_times = number_of_times[::-1]
                number_of_times = int(''.join(number_of_times))
                sentence = sentence[::-1]
                sentence = sentence * number_of_times
                stack += sentence
        
        return ''.join(stack)
                    
                    
                    