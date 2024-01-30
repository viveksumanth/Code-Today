class Solution {
    private int calculate(int number1, int number2, String operation) {
        int result = 0;
        if (operation.equals("+")) {
            result = number1+number2;
        } else if (operation.equals("-")) {
            result = number2-number1;
        } else if (operation.equals("*")) {
            result = number1*number2;
        } else if (operation.equals("/")) {
            result = number2/number1;
        }

        return result;
    }
    
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        List<String> operations = List.of("+", "-", "*", "/");
        
        for (String eachToken: tokens) {

            int number = 0;
            if (!operations.contains(eachToken)) {
                number = Integer.parseInt(eachToken);
            } else {
                int number1 = stack.pop();
                int number2 = stack.pop();
                number = calculate(number1, number2, eachToken);
            }
            stack.push(number);
        }

        return stack.get(0);
        
    }
}
