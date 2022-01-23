class Solution:
    def __init__(self):
        self.minmDigits = 0
        self.maxmDigits = 0
        self.low = 0
        self.high = 0
        self.result = set()
        
    def sequentialDigitsHelper(self,current,tempSol):
        tempNum = int(''.join(tempSol))
        
        if len(tempSol) > self.maxmDigits:
            return
        
        if int(current) > 9:
            return
        
        if self.low <= tempNum <= self.high:
            # print(tempNum)
            self.result.add(tempNum)
        
        current = str(int(current) + 1)
        if len(tempSol) < self.maxmDigits:
            tempSol += [current]
        
        self.sequentialDigitsHelper(current,tempSol)
        
        return 
        
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        self.minmDigits = len(str(low))
        self.maxmDigits = len(str(high))
        self.low = low
        self.high = high
        
        for i in range(0,9):
            self.sequentialDigitsHelper(str(i),[str(i)])
        
        return sorted(self.result)
        
        '''
        123
        234
        345
        456
        567
        678
        789
        we stop 3 digits from 7
        
        1234
        2345
        3456
        4567
        5678
        6789
        we stop 4 digits from 6
        
        12345
        23456
        34567
        45678
        56789
        we stop 5 digits from 5
        
        suppose number is 230 then 
        
        fix first digit 
            
        210 - 2300
        
        
        start with first number
        
                    func(1)
                func(2)
            func(3)
        func(4)
        above low and below high so add into result
        func(5)
        4
        5
       
        
        '''
        