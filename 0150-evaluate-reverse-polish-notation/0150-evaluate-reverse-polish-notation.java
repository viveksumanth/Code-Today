class Solution {
    private int calculate(final int number1, final int number2, final String operation) {
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
    
    public int evalRPN(final String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        final List<String> operations = List.of("+", "-", "*", "/");
        
        for (final String eachToken: tokens) {
            int number = 0;
            if (!operations.contains(eachToken)) {
                number = Integer.parseInt(eachToken);
            } else {
                final int number1 = stack.pop();
                final int number2 = stack.pop();
                number = calculate(number1, number2, eachToken);
            }
            stack.push(number);
        }

        return stack.pop();   
    }
}
