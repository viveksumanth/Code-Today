class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev = 0
        for each in bank:
            onesCount = each.count("1")
            if onesCount == 0:
                continue
            if prev != 0: 
                result += prev * onesCount
            prev = onesCount
        
        # result = 0
        # for i in range(1, len(oneCount)):
        #     result += oneCount[i-1]*oneCount[i]
        
        return result
            
        