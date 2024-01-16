class Solution {
    /*
    
    First we have a winner and loser in a match
    
    winner: 
    * we check if winner exists in lostMatch hashMap: 
        * if exists dont append in wonAllMatch set
        * if not exists append it wonAllMatch set
    
    loser:
    
    * check if loser exists in wonAllMatch set: if exists remove it.
    * add loser to hashMap if not exists, else increment loser count
    
    */
    public List<List<Integer>> findWinners(int[][] matches) {
        Map<Integer, Integer>lostMatch = new HashMap<>();
        Set<Integer>wonAllMatch = new HashSet<>();
        
        List<List<Integer>> result = new ArrayList<>();

        
        for(int[] eachMatch: matches) {
            int winner = eachMatch[0];
            int loser = eachMatch[1];
            
            // winner 
            if (!lostMatch.containsKey(winner)){
                wonAllMatch.add(winner);
            }
            
            // loser
            if (wonAllMatch.contains(loser)) {
                // remove loser
                wonAllMatch.remove(loser);
            }
            
            
            if (lostMatch.containsKey(loser)) {
                // add loser to loserMap
                lostMatch.put(loser, lostMatch.get(loser)+1);
            } else {
                lostMatch.put(loser, 1);
            }
            
        }
        
        List<Integer> winnerList = new ArrayList<>();
        for(int eachWinner: wonAllMatch) {
            winnerList.add(eachWinner);
        }
        Collections.sort(winnerList);
        result.add(winnerList);
            
        List<Integer>loserList = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : lostMatch.entrySet()) {
            int player = entry.getKey();
            int lostMatches = entry.getValue();
            
            if(lostMatches == 1) {
                loserList.add(player);
            }
        }
        Collections.sort(loserList);
        result.add(loserList);
        
        return result;
    }
}