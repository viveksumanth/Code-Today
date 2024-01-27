class Solution {
    public void reverseChars(int startIndex, int lastIndex, char[] s){
        while(startIndex < lastIndex) {
            char temp = s[startIndex];
            s[startIndex] = s[lastIndex];
            s[lastIndex] = temp;
            
            startIndex += 1;
            lastIndex -= 1;
        }
    }
    public void reverseWords(char[] s) {
        reverseChars(0, s.length -1, s);
        int lastSpace = -1;
        for(int i=0; i<s.length; i++) {
            if(s[i] == ' ') {
                reverseChars(lastSpace+1, i-1, s);
                lastSpace = i;
            }
        }
        reverseChars(lastSpace+1, s.length-1, s);
    }
}