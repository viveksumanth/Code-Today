class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] targetList = new int[2] ;
        int check;
        // System.out.println(Arrays.toString(nums));
        // System.out.println(target);
        Map<Integer, Integer> lookup = new HashMap<Integer, Integer>();
        for(int idx=0; idx < nums.length; idx++){
            check = target - nums[idx];
            if(lookup.containsKey(check)){
                targetList[1] = idx;
                targetList[0] = lookup.get(check);
            }
            
            lookup.put(nums[idx],idx);
        }
        return targetList;
    }
}