class Solution {
    public String solution(String phone_number) {
        String answer = "";
        String idx = "";
        for(int i=0; i < phone_number.length() - 4; i++) {
            idx += "*"; 
        }
        answer = idx + phone_number.substring(phone_number.length() - 4, phone_number.length());
        return answer;
    }
}