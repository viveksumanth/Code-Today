class Solution {
    public String maximumOddBinaryNumber(String s) {
        int oneCount = 0;
        char[] result = new char[s.length()];
        
        Arrays.fill(result, '0');
        for (char eachChar: s.toCharArray()) {
            if (eachChar == '1') {
                oneCount++;
            }
        }

        boolean flag = false;
        int startPointer = 0;
        int endPointer = s.length() - 1;

        while(oneCount > 0) {
            if (flag == false) {
                result[endPointer] = '1';
                endPointer--;
                flag = true;
            }  else {
                result[startPointer] = '1';
                startPointer++;
            }
            oneCount--;
        }
        return new String(result);
    }
}