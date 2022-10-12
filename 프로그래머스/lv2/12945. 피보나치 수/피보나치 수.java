class Solution {
    public int solution(int n) {
        int[] cache = new int[n+1];
        cache[0] = 0;
        cache[1] = 1;
        for (int i = 2; i < n + 1; i++) {
            cache[i] = (cache[i-1]%1234567 + cache[i-2]%1234567)%1234567;
        }
        return cache[n];
    }
}