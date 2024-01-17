class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> lookup = new HashMap<>();
        Set<Integer> uniqueValues = new HashSet<>();
        
        for (int eachNum:arr) {
            if(lookup.containsKey(eachNum)){
                lookup.put(eachNum, lookup.get(eachNum)+1);
            } else {
                lookup.put(eachNum, 1);
            }
        }
        
        for (Map.Entry<Integer, Integer> entry: lookup.entrySet()) {
            int value = entry.getValue();
            if (uniqueValues.contains(value)) {
                return false;
            } else {
                uniqueValues.add(value);
            }
        }
        
        return true;
    }
}