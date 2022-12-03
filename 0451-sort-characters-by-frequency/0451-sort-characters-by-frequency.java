class Solution {
    public String frequencySort(String s) {
        HashMap<Character,Integer> lookup = new HashMap<Character,Integer>();
        ArrayList<Integer> list = new ArrayList<>();
        String result = "";
        
        for(int i = 0; i < s.length(); i++){
            char curChar = s.charAt(i);
            
            if (lookup.containsKey(curChar)){
                lookup.put(curChar,lookup.get(curChar)+1);
            }else
                lookup.put(curChar,1);
            }
        
        //LinkedHashMap preserve the ordering of elements in which they are inserted
        LinkedHashMap<Character, Integer> reverseSortedMap = new LinkedHashMap<>();

        //Use Comparator.reverseOrder() for reverse ordering
        lookup.entrySet()
          .stream()
          .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder())) 
          .forEachOrdered(x -> reverseSortedMap.put(x.getKey(), x.getValue()));
        

        for (Character key : reverseSortedMap.keySet()) {
            while(reverseSortedMap.get(key) != 0){
                result += key;
                reverseSortedMap.put(key,reverseSortedMap.get(key)-1);
            }
        }
        
        return result;
    }
}