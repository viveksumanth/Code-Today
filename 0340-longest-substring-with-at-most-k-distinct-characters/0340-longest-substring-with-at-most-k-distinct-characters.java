class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> lookup = new HashMap<>();
        int longest = 0;
        int pointer = 0;
        for(int i = 0; i < s.length(); i++) {
            char eachChar = s.charAt(i);
            if(!lookup.containsKey(eachChar)) {
                lookup.put(eachChar, 1);
            } else {
                lookup.put(eachChar, lookup.get(eachChar)+1);
            }
            
            if (lookup.size() > k) {
                char currentChar = s.charAt(pointer);
                lookup.put(currentChar, lookup.get(currentChar)-1);
                if (lookup.get(currentChar) == 0) {
                    lookup.remove(currentChar);
                }
                pointer += 1;
            }
            
            longest = Math.max(longest, i-pointer+1);
        }
        return longest;
    }
}