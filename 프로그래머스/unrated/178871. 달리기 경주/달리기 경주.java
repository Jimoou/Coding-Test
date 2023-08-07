import java.util.HashMap;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> grade = new HashMap<>();
        for(int i = 0; i < players.length; i++) {
            grade.put(players[i],i);
        }
        for (String name : callings) {
            int idx = grade.get(name);
            String temp = players[idx];
            players[idx] = players[idx-1];
            players[idx-1] = temp;
            grade.put(players[idx], idx);
            grade.put(players[idx-1], idx-1);
        }
        return players;
    }
}