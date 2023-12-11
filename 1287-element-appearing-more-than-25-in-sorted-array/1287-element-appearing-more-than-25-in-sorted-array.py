class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        lookup = Counter(arr)
        
        maxElementCount = 0
        maxElementNumber = None
        for each in lookup:
            temp = max(maxElementCount, lookup[each])
            if temp != maxElementCount:
                maxElementNumber = each
                maxElementCount = temp

        return maxElementNumber
    
#         maxNumber = arr[0]
#         maxNumberCount = 1
#         counter = 0
#         currentNumber = arr[0]
#         for i in range(1,len(arr)):
#             if arr[i] == currentNumber:
#                 counter += 1
#             else:
#                 temp = max(maxNumberCount, counter)
#                 if temp != maxNumberCount:
#                     maxNumber = arr[i]
#                     maxNumberCount = temp
#                 counter = 1
#                 currentNumber = arr[i]
                
#             print(maxNumber, maxNumberCount)
#         return maxNumber
                
        