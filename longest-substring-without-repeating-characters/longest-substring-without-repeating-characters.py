class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        To Find distinct or not i have to remember the characters which I have already seen 
        so store them in hashmap
        
        a b c a b c b b
        1 2
        
        move pointer2 until the repeated character is found while moving also append the chracters into           hashmap
        
        {a: 0}
        {a: 0, b: 1}
        {a: 0, b: 1, c: 2}
        
        now since we hit the pointerB which is already in the array we increment
        the pointerA to the hashmap[repeated]+1 and also update the index.
        
        a b c a b c b b
                    | |  
        {a: 0}
        {a: 0, b: 1}
        {a: 3, b: 6, c: 5}
        
        so on until we reach the end of the string
        '''
        '''
        abba
        {a = 0} maxsize = 1
        {a = 0, b = 1} maxsize = 2 
        {a = 0, b = 2} maxsize = 2 pointerB - pointerA + 1 = 0
        {a = 3, b = 2} maxsize = 2
        '''
        pointerA = 0
        pointerB = 0
        hm = {}
        maxSize = float('-inf')
        
        for pointerB in range(0, len(s)):
            if s[pointerB] not in hm:
                hm[s[pointerB]] = pointerB
            
            else:
                pointerA = max(hm[s[pointerB]]+1, pointerA)
                hm[s[pointerB]] = pointerB

            maxSize = max(maxSize, pointerB - pointerA + 1)
        
        if maxSize == float('-inf'):
            return 0
        return maxSize
            
            
            
        