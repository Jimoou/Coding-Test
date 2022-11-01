import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int count = 0;
        Stack<Integer> bucket = new Stack<>();
        for (int i : moves) {
            for (int j = 0; j < board.length; j++) {
                if (board[j][i-1] != 0) {
                    if (bucket.size() > 0) {
                        if (bucket.peek() == board[j][i-1]) {
                            bucket.pop();
                            count += 2;
                        } else {
                            bucket.push(board[j][i-1]);
                        }
                    }
                    else {bucket.push(board[j][i - 1]);}
                    board[j][i-1] = 0;
                    break;
                }
            }
        }
        return count;
    }
}