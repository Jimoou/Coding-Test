import java.util.Scanner;

public class Main {
    public static int decomposition(int k) {
        int ret = k;

        while(k > 0) {
            ret = ret + k % 10;
            k = k /10;
        }

        return ret;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N, M = 0;
        N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            if (N == decomposition(i)) {
                M=i;
                break;
            }
        }


        System.out.println(M);
    }
}