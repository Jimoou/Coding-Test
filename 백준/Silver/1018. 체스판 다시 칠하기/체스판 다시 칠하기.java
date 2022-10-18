import java.util.Scanner;

public class Main {
    static int N, M;
    static String s;
    static int[][] chessBoard;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        chessBoard = new int[N][M];
        for (int i = 0; i < N; i++) {
            s = sc.next();
            for (int j = 0; j < M; j++) {
                if (s.charAt(j) == 'W') {
                    chessBoard[i][j] = 0;
                } else {
                    chessBoard[i][j] = 1;
                }
            }
        }
    int answer = 8*8;
        for (int i = 0; i+7 < N; i++) {
            for (int j = 0; j+7 < M; j++) {
                int BW = 0;
                int WB = 0;
                for (int ki = 0; ki < 8; ki++) {
                    for (int kj = 0; kj < 8; kj++) {
                        if((ki+kj) % 2 == 0 && chessBoard[i + ki][j + kj] != 1) {
                            BW++;
                        }
                        else if ((ki +kj) % 2 == 1 && chessBoard[i + ki][j + kj] != 0) {
                            BW++;
                        }
                        WB = 64 - BW;
                    }
                }
                answer = Math.min(answer,BW);
                answer = Math.min(answer,WB);
            }
        }
        System.out.println(answer);
    }
}