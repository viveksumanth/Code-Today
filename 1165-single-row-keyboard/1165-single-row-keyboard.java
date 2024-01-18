class Solution {
    public int calculateTime(String keyboard, String word) {
        Map<Character, Integer> lookup = new HashMap<>();
        int distance = 0;
        int prevCharPosition = 0;
        
        for (int i=0; i< keyboard.length(); i++) {
            char currentChar = keyboard.charAt(i);
            lookup.put(currentChar, i);
        }
        
        for (char eachChar: word.toCharArray()) {
            int currentPosition = lookup.get(eachChar);
            distance += Math.abs(currentPosition - prevCharPosition);
            prevCharPosition = currentPosition;
        }
        return distance;
    }
}