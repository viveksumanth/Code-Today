class Solution {
    
    public int numSquares(int n, Map<Integer, Integer> memo, int steps) {
        if (n == 0) {
            return steps;
        }
        
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        
        int result = 0;
        int closestMaximum = 1;
        
        List<Integer> squares = new ArrayList<>();
        
        for (int i=1; i <= n; i++) {
            if(i*i > n) {
                break;
            }
            squares.add(i*i);
            closestMaximum = i*i;
        }
        int minSteps = Integer.MAX_VALUE;
        
        for (int i=0; i < squares.size(); i++) {
            minSteps = Math.min(minSteps, numSquares(n-squares.get(i), memo, 0)) + 1;
            if (memo.containsKey(n)) {
                memo.put(n, Math.min(memo.get(n), minSteps));
            } else {
                memo.put(n, minSteps);   
            }
        }
        
        return minSteps;
    }
    public int numSquares(int n) {
        int result = 0;
        // backtracking
        var memo = new HashMap<Integer, Integer>();
        numSquares(n, memo, 0);
        return memo.get(n);
        
    }
}