import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int dollNum = 0;
        int temp = 0;
        Stack<Integer> bucket = new Stack<>();
        
        for (int i = 0; i < moves.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[j][moves[i] - 1] != 0) {
                    dollNum = board[j][moves[i] - 1];
                    bucket.push(board[j][moves[i] - 1]);
                    board[j][moves[i] - 1] = 0;
                    break;
                } else if (board[board[0].length - 1][moves[i] - 1] == 0) {
                    dollNum = 0;
                    temp--;
                    break;
                }
            }
            temp++;
            if (bucket.size() > 1) {
                if (bucket.get(temp - 2) == dollNum && dollNum != 0) {
                    bucket.pop();
                    bucket.pop();
                    temp -= 2;
                    answer += 2;
                }
            }
        }

        return answer;
    }
}