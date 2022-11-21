class Solution {
    public int removeDuplicates(int[] nums) {
        int slowP = 0;
        int fastP = 1;
        
        while(fastP < nums.length){

            
            if(nums[slowP] != nums[fastP]){
                nums[slowP+1] = nums[fastP];
                slowP += 1;
                
            }else
                fastP += 1;
        }
        
        return slowP+1;
        
    }
}