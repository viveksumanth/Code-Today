class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        String resultString = "";
        
        for (int i=words.length-1; i >= 0; i--) {
            if (words[i].length() == 0) {
                continue;
            }
            
            resultString += words[i] + " ";
        }
        return resultString.substring(0, resultString.length() - 1); 
    }
}