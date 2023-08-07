import java.util.HashMap;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        HashMap<String, Integer> score = new HashMap<>();
        for(int i = 0; i < name.length; i++) {
            score.put(name[i], yearning[i]);
        }
        for(int i = 0; i < photo.length; i++) {
            int sum = 0;
            for(String person : photo[i]) {
                sum += score.getOrDefault(person, 0);  // 사진 속 인물의 그리움 점수를 더함
            }
            answer[i] = sum;
        }
        return answer;
    }
}