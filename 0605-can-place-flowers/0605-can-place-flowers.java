class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) {
            return true;
        }
        if (flowerbed.length == 1){
            if(flowerbed[0] == 0) {
                flowerbed[0] = 1;
                n -= 1;
            }
        } 
        else {        
            for(int i = 0; i < flowerbed.length; i++) {
                
                if(n == 0) {
                    return true;
                }

                if (flowerbed[i] == 0) {
                    if (i == 0) {
                        //check i+1
                        if (flowerbed[i+1] == 0) {
                            flowerbed[i] = 1;
                            n -= 1;
                        }
                    } else if (i == flowerbed.length-1) {
                        //check i-1
                        if (flowerbed[i-1] == 0) {
                            flowerbed[i] = 1;
                            n -= 1;
                        }
                    } else {
                        if (flowerbed[i-1] == 0 && flowerbed[i+1] == 0) {
                            flowerbed[i] = 1;
                            n -= 1;
                        }
                    }
                }
            }
        }
       
        if (n == 0){
            return true;
        }
        return false;
    }
}