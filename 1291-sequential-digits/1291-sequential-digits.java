class Solution {
    public void sequentialDigits(int low, int high, List<Integer> result, int length) {
        String memo = "123456789"; 
        for (int i=0; i<memo.length()-length+1; i++){
            int newNumber = Integer.parseInt(memo.substring(i,i+length));
            if (newNumber >= low && newNumber <= high) {
                result.add(newNumber);
            }
        }
    }
    
    public List<Integer> sequentialDigits(int low, int high) {
        var result = new ArrayList<Integer>();
        int lowLength = String.valueOf(low).length();
        int highLength = String.valueOf(high).length();
        
        while(lowLength <= highLength) {
            sequentialDigits(low, high, result, lowLength);
            lowLength++;
        }
        
        return result;
    }
}