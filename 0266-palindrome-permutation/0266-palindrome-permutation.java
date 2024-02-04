class Solution {
    public boolean canPermutePalindrome(String s) {
        Map<Character,Integer> lookup = new HashMap<>();
        int oddNum = 0;

        for (int i=0; i<s.length(); i++) {
            char curChar = s.charAt(i);
            
            if(lookup.containsKey(curChar)) {
                lookup.put(curChar, lookup.get(curChar)+1);
            } else {
                lookup.put(curChar, 1);
            }
        }

        for (Map.Entry<Character,Integer> entry: lookup.entrySet()) {
            if (entry.getValue()%2 != 0) {
                oddNum += 1;
            }

            if (oddNum > 1) {
                return false;
            }
        }

        return true;

    }
}