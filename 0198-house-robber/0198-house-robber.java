class Solution {
    private int dfs(int[]nums, int currentPos, Map<Integer, Integer> memo) {
        if (currentPos == nums.length-1 || currentPos == nums.length-2) {
            return nums[currentPos];
        }
        
        if (memo.containsKey(currentPos)) {
            return memo.get(currentPos);
        }
        
        int currentMax = 0;
        for (int j=currentPos+2; j<nums.length; j++){
            currentMax = Math.max(currentMax, dfs(nums, j, memo));
        }
        memo.put(currentPos, nums[currentPos]+currentMax);
        return nums[currentPos]+currentMax;
    }
    
    public int rob(int[] nums) {
        int maxLoot = 0;
        Map<Integer, Integer> memo = new HashMap<>();
        
        for(int i=0; i<nums.length; i++) {
            maxLoot = Math.max(maxLoot, dfs(nums, i, memo));
        }
        
        return maxLoot;
    }
}