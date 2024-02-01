class Solution {
    public int[][] divideArray(int[] nums, int k) {
        int [][] result = new int[nums.length/3][3];
        Arrays.sort(nums);
        int subListFirstElement = -1;
        int inListPointer = 0;
        int outListPointer = 0;
            
        for (int i=0; i< nums.length; i++) {
            if (subListFirstElement == -1 || nums[i] - subListFirstElement <= k) {
                result[outListPointer][inListPointer] = nums[i];
                inListPointer++;
                
                if (subListFirstElement == -1) {
                    subListFirstElement = nums[i];
                }
                
                if (inListPointer > 2) {
                    inListPointer = 0;
                    subListFirstElement = -1;
                    outListPointer++;
                    
                }
            } else {
                return new int[0][0];
            }
        }
        return result;
    }
}