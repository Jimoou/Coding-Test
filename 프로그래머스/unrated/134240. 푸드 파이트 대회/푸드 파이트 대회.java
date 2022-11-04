class Solution {
    public String solution(int[] food) {
        StringBuilder left_Line = new StringBuilder();
        for (int i = 1; i < food.length; i++) {
            if (food[i] > 1) {
                left_Line.append(String.valueOf(i).repeat(food[i] / 2));
            }
        }
        return left_Line.toString()+"0"+left_Line.reverse().toString();
    }
}