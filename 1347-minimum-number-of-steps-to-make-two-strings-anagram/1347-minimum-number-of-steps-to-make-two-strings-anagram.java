class Solution {
    public int minSteps(String s, String t) {
        Map<Character, Integer> lookup = new HashMap<>();
        int count = 0;
        
        for(int i=0; i< s.length(); i++) {
            char a = s.charAt(i);
            if(lookup.containsKey(a)){
                lookup.put(a, lookup.get(a)+1);
            } else {
                lookup.put(a, 1);
            }
        }
        
        for(int j = 0; j<s.length(); j++) {
            char b = t.charAt(j);
            if (lookup.containsKey(b)) {
                lookup.put(b, lookup.get(b)-1);
                if (lookup.get(b) == 0){
                    lookup.remove(b);
                }
            } else {
                count += 1;
            }
        }
        
      return count;  
    }
}