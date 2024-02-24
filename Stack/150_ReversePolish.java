class Solution {
    public int evalRPN(String[] tokens) {
        Stack <Integer> stack = new Stack();
        int op1;
        int op2;
        int result;

        for (int i = 0; i<tokens.length; i++){
            if (tokens[i].equals("+")){
                op1 = stack.pop();
                op2 = stack.pop();
                result = op1 + op2;
                stack.push(result);
            }
            else if (tokens[i].equals("-")){
                op1 = stack.pop();
                op2 = stack.pop();
                result = op2 - op1;
                stack.push(result);
            }
            else if (tokens[i].equals("*")){
                op1 = stack.pop();
                op2 = stack.pop();
                result = op1 * op2;
                stack.push(result);
            }
            else if (tokens[i].equals("/")){
                op1 = stack.pop();
                op2 = stack.pop();
                result = op2 / op1;
                stack.push(result);
            }
            else {
                stack.push(Integer.parseInt(tokens[i]));
            }
        }

        return stack.peek();
    }
}