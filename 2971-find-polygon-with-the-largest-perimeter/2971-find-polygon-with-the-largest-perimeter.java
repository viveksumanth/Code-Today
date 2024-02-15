class Solution {
    public long largestPerimeter(int[] nums) {
        /*
        [1,12,1,2,5,50,3]
        [1,1,2,3,5,12,50]
        [1,1,2] 
        [1,1,2,3,5]
        [1,1,2,3,5,12]
        
        sort the list
        * start adding the elements untill we reach 2 
        * once we reach 2 or greater than 2 elements then we check if the nextElement is <= currentSum
        * if yes we compare it with existing maximum
        * else if just move forward.
        */

        Arrays.sort(nums);
        long largestPerimeterSum = -1;
        long previousSum = 0;

        for(int i=0; i<nums.length; i++) {
            
            if (i >= 2) {
                // check i+1 is < sum of other sides
                if (nums[i] < previousSum) {
                    largestPerimeterSum = previousSum + nums[i];
                }
            }
           previousSum += nums[i];
        }

        return largestPerimeterSum;
    }
}