	# diffs = [b-a for a, b in zip(A, A[1:])]
	# l = r = cnt = 0  # left, right pointers and counter
	# while r < len(diffs):
	# 	if diffs[r] == diffs[l]: 
	# 		cnt += r - l
	# 	else: 
	# 		l = r
	# 	r += 1
	# return cnt

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        store = []
        count = 0
        
        for idx in range(1,len(nums)):
            store.append(nums[idx] - nums[idx - 1])

        pointer = 0
        newIdx = 1

        while(newIdx < len(nums) - 1):

            if store[newIdx-1] == store[newIdx]:
                count += newIdx - pointer
            else:
                pointer = newIdx
            
            newIdx += 1
            
        return count
        
        
                    
                
            
        
        
        