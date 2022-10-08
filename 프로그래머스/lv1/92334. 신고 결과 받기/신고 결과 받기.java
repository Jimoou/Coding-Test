import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];

        HashMap<String, HashSet<String>> ht = new HashMap<>();
        HashMap<String, Integer> hm = new HashMap<>();

        for (int i = 0; i < id_list.length; i++) {
            String name = id_list[i];
            ht.put(name, new HashSet<>());
            hm.put(name, i);
        }

        for (String s : report) {
            String[] str = s.split(" ");
            String from = str[0];
            String to = str[1];
            ht.get(to).add(from);
        }

        for (int i = 0; i < id_list.length; i++) {
            HashSet<String> reported = ht.get(id_list[i]);
            if (reported.size() >= k) {
                for (String name : reported) {
                    answer[hm.get(name)]++;
                }
            }
        }

        return answer;
    }
}