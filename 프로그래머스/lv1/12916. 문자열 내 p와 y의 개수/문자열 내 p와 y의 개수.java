class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int cntP = 0;
        int cntY = 0;
        char ch = ' ';
        
        for (int i = 0; i < s.length(); i++) {
			ch = s.charAt(i);
			if(ch == 'p' || ch == 'P') {
                cntP++;
            } else if (ch == 'y' || ch == 'Y') {
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