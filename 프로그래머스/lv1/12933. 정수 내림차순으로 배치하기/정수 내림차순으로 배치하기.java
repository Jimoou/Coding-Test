import java.util.*;
import java.io.*;

class Solution {
    public long solution(long n) {
        String s = Long.toString(n);
        String[]  arr = s.split("");
        long answer;
        Arrays.sort(arr, Collections.reverseOrder());
        String tmp = String.join("",arr);
        answer = Long.parseLong(tmp);
        System.out.println((answer));
        return answer;
    }
}