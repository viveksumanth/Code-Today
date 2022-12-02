class Solution {
    public boolean closeStrings(String word1, String word2) {

        char[] word1Array = new char[26];
        char[] word2Array = new char[26];

        for(int i = 0; i < word1.length(); i++){
            char curChar1 = word1.charAt(i);

            word1Array[curChar1 -'a']++;
        }
        for(int j = 0; j < word2.length(); j++){
            char curChar2 = word2.charAt(j);
            word2Array[curChar2 -'a']++;
        }
        

        
        for(int i = 0; i<26; i++){
            if(word1Array[i]!=0 && word2Array[i] == 0){
                return false;
            }
            else if (word1Array[i] == 0 && word2Array[i] != 0){
                return false;
            }
        }
        
        Arrays.sort(word1Array);
        Arrays.sort(word2Array);
        
        for(int i=0;i<26;i++){
            if(word1Array[i]!=word2Array[i]){
                return false;
            }
        }
        return true;
    }
}
        