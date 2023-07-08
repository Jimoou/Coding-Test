class Solution {
    public int solution(int a, int b) {
        String strA = Integer.toString(a);
        String strB = Integer.toString(b);
        String strAB = strA + strB;
        String strBA = strB + strA;
        int AB = Integer.parseInt(strAB);
        int BA = Integer.parseInt(strBA);
        return (AB >= BA) ? AB : BA;
    }
}