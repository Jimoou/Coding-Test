import java.util.Arrays;

class Solution {
    public static int solution(int[][] lines) {
        int[] start = new int[lines.length];
        int[] end = new int[lines.length];
        for (int i = 0; i < lines.length; i++) {
            start[i] = Math.min(lines[i][0], lines[i][1]);
            end[i] = Math.max(lines[i][0], lines[i][1]);
        }
        Arrays.sort(start);
        Arrays.sort(end);
        int answer = 0;
        answer += Math.max(0, end[0] - start[1]);
        answer += Math.max(0, end[1] - start[2]);
        answer -= Math.max(0, end[0] - start[2]);

        return answer;
    }
}