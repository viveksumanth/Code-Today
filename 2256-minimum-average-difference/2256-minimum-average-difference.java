class Solution {
    public int minimumAverageDifference(int[] nums) {
        

        int minIdx = 0;
        long minDiff = Integer.MAX_VALUE;
        long pSum = 0;
        long fHalf = 0 ;
        long sHalf = 0;
        long curDiff;
        long curNum = 0;
        long div;
        int curMin = 0;
        int length = nums.length;
        
        for(int i=0; i<nums.length; i++){
            pSum += nums[i];
        }
        
        for(int idx = 0; idx < nums.length; idx++){
            
            curNum += nums[idx];
            div = idx+1;
            
            fHalf = curNum/div;
            
            if ((length - div)!= 0){
                sHalf = (pSum - curNum)/(length-div);
            }else
                sHalf = 0;
            
            curDiff = Math.abs(fHalf-sHalf);
                
            if (curDiff < minDiff){
                minDiff = curDiff;
                minIdx = idx;
            }
        }
        
        return minIdx;
    }
}