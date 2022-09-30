import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int key = stages.length;
        
        HashMap<Integer, Double> map = new HashMap<>();
        
        for (int i = 1; i <= N; i++) {
            int cnt = 0;
            for (int j = 0; j < stages.length; j++) {
                if (stages[j] == i) {
                    cnt++;
                }
            }
            if (cnt == 0) {
                map.put(i, 0.0);
            } else {
                map.put(i, (double)cnt/key);
            }
            key = key - cnt;
        }    
        List<Integer> list = new ArrayList<>(map.keySet());
        Collections.sort(list, (o1, o2) -> Double.compare(map.get(o2), map.get(o1)));
        
        
    return list.stream().mapToInt(Integer::intValue).toArray();
    }
}