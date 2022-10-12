class Solution {
    public String solution(String s) {
        String answer = "" + s.toUpperCase().charAt(0);

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i - 1) == ' ' && s.charAt(i) != ' ') {
                answer += s.toUpperCase().charAt(i);
            }
            else {
                answer += s.toLowerCase().charAt(i);
            }
        }
        return answer;
    }
}