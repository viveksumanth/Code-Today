class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
       permsList = list(itertools.permutations(digits, 3))
       
       resultSet = set()

       for each in permsList:
            if each[2]%2 == 0 and each[0] != 0:
                resultSet.add(each)
        

       return len(resultSet)
            


       
        
