/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface BinaryMatrix {
 *     public int get(int row, int col) {}
 *     public List<Integer> dimensions {}
 * };
 */

class Solution {
    
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
        
        List<Integer> dimensions = binaryMatrix.dimensions();
        int rowSize = dimensions.get(0);
        int colSize = dimensions.get(1);
        
        int left = 0;
        int right = colSize;
        int minimum = Integer.MAX_VALUE;
        
        while (left < right) {
            // System.out.println(left);
            // System.out.println(right);
            int mid = (left + right)/2;
            // System.out.println(mid);
            boolean foundOne = false;
            
            for (int i=0; i<rowSize; i++) {
                if (binaryMatrix.get(i,mid) == 1) {
                    minimum = mid;
                    foundOne = true;
                    break;
                }
            }
            
            if (foundOne == true) {
                right = mid;
            } else {
                left = mid + 1;
            }      
        }
        if (minimum == Integer.MAX_VALUE) {
            return -1;
        }
        return minimum;
    }
}