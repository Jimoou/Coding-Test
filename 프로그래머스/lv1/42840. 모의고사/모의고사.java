import java.util.*;


class Solution {
    public int[] solution(int[] answers) {

        int[] no1Ans = {1, 2, 3, 4, 5};
        int[] no2Ans = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] no3Ans = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] score = new int[3];
        
        for (int i = 0; i < answers.length; i++) {
            if (no1Ans[i%no1Ans.length] == answers[i]) {
                    score[0]++;
            }
            if (no2Ans[i%no2Ans.length] == answers[i]) {
                    score[1]++;
            }
            if (no3Ans[i%no3Ans.length] == answers[i]) {
                    score[2]++;
            }
        }

        int maxScore = Math.max(score[0], Math.max(score[1], score[2]));
        ArrayList<Integer> list = new ArrayList<>();
        if(maxScore == score[0]) {
            list.add(1);
        }
        if(maxScore == score[1]) {
            list.add(2);
        }
        if(maxScore == score[2]) {
            list.add(3);
        }
        
        return list.stream().mapToInt(i->i.intValue()).toArray();
    }
}