class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        word 1 is <= word2
        '''
        # if len(word1) > len(word2):
        #     temp = word1
        #     word1 = word2
        #     word2 = temp
        
        pointer = 0
        result = []
        
        while(pointer < len(word1) and pointer < len(word2)):
            result.append(word1[pointer])
            result.append(word2[pointer])
            pointer += 1
        
        if len(word1) > pointer:
            result.append(word1[pointer::])
        elif len(word2) > pointer:
            result.append(word2[pointer::])

        return ''.join(result)
