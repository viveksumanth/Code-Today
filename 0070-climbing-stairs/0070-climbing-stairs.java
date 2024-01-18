class Solution {

    private int dfs(int currentState, int n, Map<Integer, Integer> memo){ 
        if (currentState == n){
            return 1;
        }
        
        if (memo.containsKey(currentState)) {
            return memo.get(currentState);
        }
        
        int oneStepWay = 0;
        if(currentState+1 <= n) {
            oneStepWay = dfs(currentState+1, n, memo);
        }
        
        int twoStepWay = 0;
        if (currentState+2 <= n) {
            twoStepWay = dfs(currentState+2, n, memo);
        } 
        
        memo.put(currentState, oneStepWay+twoStepWay);
        return memo.get(currentState);
    }
    
    public int climbStairs(int n) {
        Map<Integer, Integer> memo = new HashMap<>();
        return dfs(0,n, memo);
    }
}