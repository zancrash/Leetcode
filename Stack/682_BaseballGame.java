class Solution {
    public int calPoints(String[] operations) {
        int score = 0;
        Stack<Integer> records = new Stack();
        int l = operations.length;

        for (int i = 0; i<l; i++){
            if (operations[i].equals("+")){
                int top = records.pop();
                int newScore = top + records.peek();
                records.push(top);
                records.push(newScore);
            }
            else if (operations[i].equals("D")){
                int newScore = records.peek() * 2;
                records.push(newScore);
            }
            else if (operations[i].equals("C")){
                records.pop();
            }
            else {
                records.push(Integer.parseInt(operations[i]));
            }
        }
        while (!records.isEmpty()){
            score += records.pop();
        }

        return score;
    }
}