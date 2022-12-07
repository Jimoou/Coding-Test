class Solution {
    public int solution(String s) {
        int result = 0;
        int cnt1 = 0;
        int cnt2 = 0;
        char start = ' ';

        for (int i = 0; i < s.length(); i++) {
            if (start == ' ') {start = s.charAt(i);}
            if (start == s.charAt(i)) {cnt1++;}
            else {cnt2++;}
            if (cnt1 == cnt2) {
                result++;
                cnt1 = 0;
                cnt2 = 0;
                start = ' ';
            }
        }
        if (start != ' ') {result++;}

        return result;
    }
}