class Solution {
    public boolean halvesAreAlike(String s) {
        
        Set<Character>vowels = new HashSet<Character>();
        
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
        
        // divide the string into 2 halfs and count number of vowels
        int strLength = s.length();
        int firstHalf = 0;
        int secondHalf = 0;
        
        for(int idx = 0; idx<strLength;idx++){

            if(idx < (strLength/2)){
                //count vowels
                if(vowels.contains(s.charAt(idx))){
                     secondHalf += 1;
                }
            }else
                if(vowels.contains(s.charAt(idx))){
                    firstHalf += 1;
                    
                }
            // System.out.println(s.charAt(idx));
            // System.out.println(firstHalf);
            // System.out.println(secondHalf);   
            // System.out.println("");
        }

        if(firstHalf == secondHalf){
            return true;
        };
        
        return false;
    }
}