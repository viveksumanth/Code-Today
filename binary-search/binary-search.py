class Solution:
    
    def Compute_binary_search(self,nums,l,r,target):
        
        if r >= l:

            mid = (l + r) //2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                return self.Compute_binary_search(nums,mid+1,r,target)
            
            elif nums[mid] > target:
                return self.Compute_binary_search(nums,l,mid-1,target)
            
        else:  
            return -1
        
    
    def search(self, nums: List[int], target: int) -> int:
        
        # if(len(nums)==1 and target==nums[0]):
        #     return 0
        
        return self.Compute_binary_search(nums,0,len(nums)-1,target)
        
        #Binary Search
        