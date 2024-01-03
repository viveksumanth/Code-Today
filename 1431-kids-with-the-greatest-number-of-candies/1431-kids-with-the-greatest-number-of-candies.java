class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maximumCandies = Arrays.stream(candies).max().getAsInt();
        List<Boolean> result = new ArrayList<>();
        
        for (int eachCandy: candies){
            if(eachCandy + extraCandies >= maximumCandies) {
                result.add(true);
            } else{
                result.add(false);
            }
        }
        
        return result;
    }
}