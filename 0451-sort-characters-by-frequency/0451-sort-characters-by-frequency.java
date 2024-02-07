class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> lookup = new HashMap<>();
        
        for (char eachChar:s.toCharArray()) {
            if (lookup.containsKey(eachChar)) {
                lookup.put(eachChar, lookup.get(eachChar)+1);
            } else {
                lookup.put(eachChar, 1);
            }
        }
        
        // covert map to list
        List<Map.Entry<Character, Integer>> list = new ArrayList<>(lookup.entrySet());
        
        list.sort(new Comparator<>(){
            public int compare(Map.Entry<Character, Integer> o1, Map.Entry<Character, Integer> o2) {
                return (o2.getValue()).compareTo(o1.getValue());
            }
        });
        
        StringBuilder result = new StringBuilder();
        
        for (Map.Entry<Character, Integer> entry : list) {
            for (int i=0; i < entry.getValue(); i++) {
                result.append(entry.getKey()); 
            }
        }

        return result.toString();
    }
}