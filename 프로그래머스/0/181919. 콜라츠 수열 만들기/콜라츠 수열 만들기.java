import java.util.*;
class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        list.add(n);
        while(n != 1){
            if (n % 2 == 0) {
                n = n / 2;
            } else if (n % 2 == 1) {
                n = 3 * n + 1;
            }
            list.add(n);
        }
        return listToArray(list);
    }
    public int[] listToArray(List<Integer> list) {
        int[] arr = new int[list.size()];
        for (int i = 0 ; i < list.size() ; i++) 
            arr[i] = list.get(i).intValue();
        return arr;
    }
}