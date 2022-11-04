class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int cntP = 0;
        int cntY = 0;
        
        for (int i = 0; i < s.length(); i++) {
	    String word = String.valueOf(s.charAt(i));
	    if("p".equalsIgnoreCase(word)) {
                cntP++;
            } else if ("y".equalsIgnoreCase(word)) {
                cntY++;
            }
        }
        if (cntP == cntY) {
            answer = true;
        } else {
            answer = false;
        }
        return answer;
    }
}
