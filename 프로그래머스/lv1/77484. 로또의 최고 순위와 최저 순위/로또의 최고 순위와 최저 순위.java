class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        
        int[] arr = new int[2];
        int temp = 0;
        int cnt = 0;
        int num = 0;
        
        for(int i : lottos) {
            for(int c : win_nums) {
                if (i == c) {
                    cnt++;
                }
            }
            if (i == 0){
                temp++;
            }
        }
        
        for (int i = 6; i > 0; i--) {
            num++;
            if (temp + cnt == 0) {
                arr[0] = 6;
                arr[1] = 6;
                break;
            }
            
            
            if (temp + cnt == i) {
                arr[0] = num;
            }
            if (cnt == i) {
                arr[1] = num;
            }
            if (cnt == 0) {
                arr[1] = 6;
                arr[0] = 1;
            }
        }
        return arr;
    }
}