class Solution {
    public boolean isOneEditDistance(String s, String t) {
        /*
        ab ba
        replacing 
        
        */
        
        int pointerS = 0;
        int pointerT = 0;
        int change = 0;
        
        if (s.length() > t.length()) {
            String temp = s;
            s = t;
            t = temp;
        }
        
        if (t.length() - s.length() > 1) {
            return false;
        }
        
        while(pointerS < s.length()) {
            if (s.charAt(pointerS) == t.charAt(pointerT)) {
                pointerS++;
                pointerT++;
            } else {
                change++;
                if (s.length() == t.length()) {
                    pointerT++;
                    pointerS++;
                } else {
                   pointerT++; 
                }
                
                if (change > 1) {
                    return false;
                }
            }
        }
        
        if (change == 0 && (t.length() - s.length()) == 1 ) {
            return true;
        }
        
        if(change == 1) {
            return true;
        }
        return false;
    }
}