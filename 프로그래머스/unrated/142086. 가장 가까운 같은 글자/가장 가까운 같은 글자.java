import java.util.*;
class Solution {
    public int[] solution(String s) {
        int[] result = new int[s.length()];

        HashMap<Character,Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!map.containsKey(s.charAt(i))) {
                result[i] = -1;
            }
            else {
                int index = map.get(s.charAt(i));
                result[i] = i - index;
            }
            map.put(s.charAt(i), i);

        }
        return result;

    }
}