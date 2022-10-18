import java.util.Scanner;

public class Main {
    static int N, ans;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        for (int i = 1; i <= N; i++) {
            if (func(i)) {
                ans++;
            }
        }
        System.out.println(ans);
    }
    static int getCipher(int n) {
        int ret = 0;
        while (n != 0) {
            ret = ret + 1;
            n = n / 10;
        }
        return ret;
    }
    static boolean func (int n) {
        int k = getCipher(n);
        int small = n % 10;
        n = n/10;
        int big = n % 10;
        int gap = big - small;
        if (k <= 2) return true;

        for (int i = 0; i < k -2; i++) {
            small = big;
            big = (n / 10) % 10;
            if (gap != big - small) return false;
            n = n / 10;
        }
        return true;
    }
}