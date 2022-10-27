class Solution {
    public static int solution(int[] number) {
        int answer = 0;
        for (int i = 0; i < number.length-2; i++) {
            for (int j = i+1; j < number.length-1; j++) {
                for (int k = j+1; k < number.length; k++) {
                    if (0 == additionNum(number, i, j, k)) {
                        answer++;
                    }
                }
            }
        }
        return answer;
    }

    static int additionNum(int[] number, int n1, int n2, int n3){
        int sum = 0;
        for (int i = 0; i < number.length; i++) {
            if (i == n1 || i == n2 || i == n3) {
                sum += number[i];
            }
        }
        return sum;
    }
}