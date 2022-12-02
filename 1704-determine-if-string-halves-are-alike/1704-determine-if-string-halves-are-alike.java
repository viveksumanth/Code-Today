class Solution {
    public boolean halvesAreAlike(String s) {
        
        Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        
        // divide the string into 2 halfs and count number of vowels
        int strLength = s.length();
        int firstHalf = 0;
        int secondHalf = 0;
        
        for(int idx = 0; idx<strLength;idx++){
            
            if(idx < (strLength/2)){
                //count vowels
                if(vowels.contains(s.charAt(idx))){
                     firstHalf += 1;
                }
            }else
                if(vowels.contains(s.charAt(idx))){
                    secondHalf += 1;
                    
                }
        }

        if(firstHalf == secondHalf){
            return true;
        };
        
        return false;
    }
}