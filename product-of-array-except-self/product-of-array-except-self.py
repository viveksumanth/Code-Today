class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        productArray = []
        prefixForward = [1]
        prefixBackward = [1]
        
        for idx in range(0,len(nums)):
            prefixForward.append(prefixForward[-1]*nums[idx]) # [1,4,20,20,160,320]
        
        for idx in range(len(nums)-1, -1, -1):  # [1,2,16,16,80,320]
            prefixBackward.append(prefixBackward[-1] * nums[idx])
        
        prefixBackward = prefixBackward[::-1]
        
        for idx in range(1,len(prefixBackward)):
            productArray.append(prefixForward[idx-1] * prefixBackward[idx])
        
        return productArray
            
            
        
        
        