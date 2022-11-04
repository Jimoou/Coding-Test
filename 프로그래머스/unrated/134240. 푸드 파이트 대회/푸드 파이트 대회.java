class Solution {
    public String solution(int[] food) {
        StringBuilder left_Line = new StringBuilder();
        StringBuilder right_Line = new StringBuilder();
        for (int i = 1; i < food.length; i++) {
            if (food[i] > 1) {
                left_Line.append(String.valueOf(i).repeat(food[i]/2));
                right_Line.append(String.valueOf(i).repeat(food[i]/2));
            }
        }
        left_Line.append(0);
        return left_Line.toString() + right_Line.reverse();
    }
}