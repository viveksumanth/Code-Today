class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] result = {0,0};
        int repeatingNum = 0;
        for (int i= 0; i<nums.length; i++) {
            while(nums[i] != i+1) {
                // replace and check
                int currentNumber = nums[i];
                if (nums[currentNumber-1] == currentNumber){
                    repeatingNum = currentNumber;
                    break;
                }
                int temp = nums[currentNumber-1];
                nums[currentNumber-1] = nums[i];
                nums[i] = temp;  
                // System.out.println(Arrays.toString(nums));
            }
        }
        
        // System.out.println(repeatingNum);
        
        int sum = 0;
        for (int number : nums) {
            sum += number;
        }
        
        int expectedSum = (nums.length * (nums.length + 1))/2;
        // System.out.println(expectedSum);
        
        int missingNum = Math.abs(expectedSum - sum + repeatingNum); 
        
//         System.out.println(missingNum);
        result[0] = repeatingNum;
        result[1] = missingNum;
        return result;
    }
}