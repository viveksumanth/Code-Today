class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        

        Map<String, List<String>> map = new HashMap<>();
        String sortedWord;
        char[] tempArray;
        
        for(String eachString:strs){
            
            tempArray = eachString.toCharArray();
            Arrays.sort(tempArray);
            
            sortedWord = new String(tempArray);
            
            
            // adding into Hashmap
            if(!map.containsKey(sortedWord)){
                map.put(sortedWord,new ArrayList<String>());
            }
            map.get(sortedWord).add(eachString);
        }
        
        
        return new ArrayList<>(map.values());
    }
}