import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public int[] solution(int k, int[] score) {
        ArrayList<Integer> honor = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            if (i > k- 1) {
                if (score[i] > honor.get(0)) {
                    honor.add(score[i]);
                    honor.remove(honor.get(0));
                }
            }
            else{
                honor.add(score[i]);
            }
            Collections.sort(honor);
            result.add(honor.get(0));
        }
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;

    }
}