class Solution {
    private Set<List<Integer>> result = new HashSet<>();

    private void dfs(int[] nums, List<Integer> currentResult, boolean[] used) {
        if(currentResult.size() == nums.length) {
            // deepCopy
            var newList = new ArrayList<>(currentResult);
            result.add(newList);       
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (used[i] == true) {
                continue;
            } 

            used[i] = true;
            currentResult.add(nums[i]);
            dfs(nums, currentResult, used);
            currentResult.remove(currentResult.size()-1);
            used[i] = false;
        }
        return;
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        boolean[] used = new boolean[nums.length];
        Arrays.fill(used, false);
        dfs(nums, new ArrayList<Integer>(), used);
        return new ArrayList(result);

    }
}