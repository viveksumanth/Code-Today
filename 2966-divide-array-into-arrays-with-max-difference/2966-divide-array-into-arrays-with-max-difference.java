class Solution {
    public int[][] divideArray(int[] nums, int k) {
        int [][] result = new int[nums.length/3][3];
        Arrays.sort(nums);
            
        for (int i=0; i< nums.length; i+=3) {
            if (nums[i+2] - nums[i] > k) {
                return new int[0][0];
            }
            result[i/3] = new int[]{nums[i], nums[i+2], nums[i+1]};
        }
        return result;
    }
}