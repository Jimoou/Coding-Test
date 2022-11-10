import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public int solution(int k, int m, int[] score) {
        int sum = 0;
        List<Integer> appleScores = Arrays.stream(score).boxed().collect(Collectors.toList());
        Collections.sort(appleScores);
        for (int pack = m; pack <= score.length; pack+=m) {
            List<Integer> box = appleScores.subList(score.length-pack, score.length-pack+m);
            sum += Collections.min(box)*m;
        }
        return sum;
}
}
