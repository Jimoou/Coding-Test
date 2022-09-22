class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        
        long num = 0;
        long sum =0;
        if (a == b) {
            return a;
        } else if (a < b) {
            for (int i = a + 1; i < b; i++) {
                num += i;
            }
        } else if (a > b) {
            for (int i = a - 1; i > b; i--) {
                num += i;
            }
        }
        sum = num + a + b;
        return sum;
    }
}