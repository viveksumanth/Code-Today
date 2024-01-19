class Solution {
	
    private static List<List> moves;
    
    private List<List<Integer>> getMoves(int row, int col, int rowLength, int colLength) {
        List<List<Integer>> nextMoves = new ArrayList<>();
        
        for(int k = 0; k < moves.size(); k++) {
            List<Integer> nextRowCol= moves.get(k);
            int nextRow = nextRowCol.get(0) + row;
            int nextCol = nextRowCol.get(1) + col;
            
            if(0 <= nextRow && nextRow < rowLength && 0 <= nextCol && nextCol < colLength) {
                List<Integer> nextMove = Arrays.asList(nextRow, nextCol);
                nextMoves.add(nextMove);
            }
        }
        return nextMoves;
    }
    
    private int dfs(List<Integer> cPos, int[][] matrix, Map<List,Integer> memo) {
        int row = cPos.get(0);
        int col = cPos.get(1);
        
        if (memo.containsKey(cPos)){
            return memo.get(cPos);
        }
        
        List<List<Integer>> nextMoves = getMoves(row, col, matrix.length, matrix[0].length);
        if (nextMoves.size() == 0) {
            memo.put(Arrays.asList(row,col), matrix[row][col]);
            return matrix[row][col];
        }
        
        int minimumPath = Integer.MAX_VALUE;
        for(final List<Integer> eachMove: nextMoves) {
            minimumPath = Math.min(minimumPath, dfs(eachMove, matrix, memo));
        }
        memo.put(cPos, minimumPath+matrix[row][col]);
        return matrix[row][col] + minimumPath;
        
        }
    
    public int minFallingPathSum(int[][] matrix) {
        moves = new ArrayList<>();
        List<Integer>move1 = Arrays.asList(1,-1);
        List<Integer>move2 = Arrays.asList(1,0);
        List<Integer>move3 = Arrays.asList(1,1);

        moves.add(move1);
        moves.add(move2);
        moves.add(move3);
        
        Map<List, Integer> memo = new HashMap<>();
        int minimumPath = Integer.MAX_VALUE;
        
        for(int i = 0; i < matrix.length; i++) {
            List<Integer> pos = Arrays.asList(0,i);
            int min = dfs(pos, matrix, memo);
            minimumPath = Math.min(minimumPath, min);
            memo.put(pos, minimumPath);
        }
        
        return minimumPath;
    }
}