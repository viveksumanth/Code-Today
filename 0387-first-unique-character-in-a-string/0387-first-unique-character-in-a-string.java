class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> lookup = new HashMap<>();
        
        for (int i=0; i<s.length(); i++) {
            char currentChar = s.charAt(i);
        
            if(lookup.containsKey(currentChar)) {
                lookup.put(currentChar, lookup.get(currentChar)+1);
            } else {
                lookup.put(currentChar, 1);
            }
        }
        
        for (int i=0; i<s.length(); i++) {
            char currentChar = s.charAt(i);
            if (lookup.get(currentChar) == 1) {
                return i;
            }
        }
        return -1;
    }
}