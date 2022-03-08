
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        mid=min(k,nums[0]-1)
        ans=((mid+1)*(mid))//2
        k-=mid
        for i in range(1,len(nums)):
            if(k==0):
                break
            if(nums[i]-nums[i-1]>1):
                mid=min(nums[i]-nums[i-1]-1,k)
                k-=mid
                ans+=(((nums[i-1]+mid+1)*(nums[i-1]+mid))//2)-(((nums[i-1]+1)*(nums[i-1]))//2)
        ans+=(((nums[len(nums)-1]+k+1)*(nums[len(nums)-1]+k))//2)-(((nums[len(nums)-1]+1)*(nums[len(nums)-1]))//2)
        return ans
            
                
            
            
            
        

            
                