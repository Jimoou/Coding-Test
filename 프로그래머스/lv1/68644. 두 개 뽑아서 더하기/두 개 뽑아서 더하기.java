import java.util.*;
class Solution {
    public Set<Integer> solution(int[] numbers) {
        Set<Integer> set = new TreeSet<>();
        for(int i = 0; i < numbers.length; i++) {
            for(int j = 0; j < numbers.length; j++) {
                if(i <= j) {
                    continue;
                }
                set.add(numbers[i] + numbers[j]);
            }
        }
        
        return set;
    }
}
