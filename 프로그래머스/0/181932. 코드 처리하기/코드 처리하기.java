import java.util.*;
class Solution {
    public String solution(String code) {
        StringBuilder ret = new StringBuilder();
        int mode = 0;
        for (int i = 0; i < code.length(); i++) {
            if (code.charAt(i) == '1'){
                mode = 1 - mode;
                continue;
            }
            if((mode == 0 && i % 2 == 0) || (mode == 1 && i % 2 == 1)) {
                ret.append(code.charAt(i));
            }
        }
        return ret.length() == 0 ? "EMPTY" : ret.toString();
    }
}