import java.util.*;
class Solution {
    //다른 인터페이스를 사용하면 시간초과가 난다ㅣ
    public String solution(String X, String Y) {
        StringBuilder answer = new StringBuilder();
        TreeMap<Character, Integer> htX = new TreeMap<>(Collections.reverseOrder());
        TreeMap<Character, Integer> htY = new TreeMap<>(Collections.reverseOrder());
        for (char s : X.toCharArray()) {
            Integer count = htX.get(s);
            if (count == null) {
                htX.put(s, 1);
            } else {
                htX.put(s, count + 1);
            }

        }

        for (char s : Y.toCharArray()) {
            Integer count = htY.get(s);
            if (count == null) {
                htY.put(s, 1);
            } else {
                htY.put(s, count + 1);
            }
        }
        
        int cnt = 0;
        for(Map.Entry<Character, Integer> e : htX.entrySet()) {
            if (htY.containsKey(e.getKey())) {
                while (htY.get(e.getKey()) > 0 && htX.get(e.getKey()) > 0) {
                    answer.append(e.getKey());
                    htX.put(e.getKey(), htX.get(e.getKey()) - 1);
                    htY.put(e.getKey(), htY.get(e.getKey()) - 1);
                }
            }
        }

        if (answer.length() == 0) {
            return "-1";
        } else if (answer.charAt(0) == '0') {
            return "0";
        }

        return answer.toString();
    }
}
