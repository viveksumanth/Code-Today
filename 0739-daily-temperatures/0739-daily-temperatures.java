class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        var stack = new ArrayList<Integer>();
        int[] result = new int[temperatures.length]; 
        
        for (int i=0; i<temperatures.length; i++) {
            if(stack.size() > 0) {
                while (stack.size() > 0 && temperatures[i] > temperatures[stack.get(stack.size()-1)]) {
                    int element = stack.remove(stack.size()-1);
                    result[element] = i-element;
                }
            }
            stack.add(i);
        }

        return result;
    }
}