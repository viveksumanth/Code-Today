class Solution {
    public boolean halvesAreAlike(String s) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        vowels.add('A');
        vowels.add('E');
        vowels.add('I');
        vowels.add('O');
        vowels.add('U');
        
        int midIndex = s.length()/2;
        int leftVowelCount = 0;
        int rightVowelCount = 0;
        
        for(int i=0; i<midIndex; i++) {
            if(vowels.contains(s.charAt(i))) {
                leftVowelCount++;
            }
        }
        
        for (int i=midIndex; i< s.length(); i++) {
            if (vowels.contains(s.charAt(i))) {
                rightVowelCount++;
            }
        }
        
        return leftVowelCount == rightVowelCount;
    }
}