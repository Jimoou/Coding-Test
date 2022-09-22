import java.util.List;
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        int intMin = arr[0];
        List<Integer> list = new ArrayList<>();

        for(int i : arr) {
            intMin = Math.min(i, intMin);
        }

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != intMin) {
                list.add(arr[i]);
            }
        }
        if (list.size() == 0) { 
            list.add(-1);
        }

        
        return list.stream().mapToInt(i -> i).toArray();
    }
}