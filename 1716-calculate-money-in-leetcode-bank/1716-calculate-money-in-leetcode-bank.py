class Solution:
    def totalMoney(self, n: int) -> int:
        numberOfWeeks = n//7
        leftDaysInWeek = n%7
        total = 0
        current = 7
        
        for i in range(0,numberOfWeeks):
            total += ((current*(current+1))//2) - ((i*(i+1))//2)
            current += 1
        
        for i in range(0,leftDaysInWeek):
            total += numberOfWeeks + 1 + i
        return total 
        