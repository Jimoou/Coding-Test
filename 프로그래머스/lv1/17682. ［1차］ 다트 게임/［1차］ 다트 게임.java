class Solution {
    public int solution(String dartResult) {
        int i = 0;
        int j = 0;
        int num = 0;
        int sum = 0;
        int[] arr = new int[3];

        while (i < dartResult.length()) {
            if (Character.isDigit(dartResult.charAt(i)) && Character.isDigit(dartResult.charAt(i + 1))) {
                num = Integer.valueOf(dartResult.substring(i, i + 2));
                i += 2;
            } else if (Character.isDigit(dartResult.charAt(i))) {
                num = Character.getNumericValue(dartResult.charAt(i));
                i++;
            }
            if (dartResult.charAt(i) == 'S') {
                    num = (int) Math.pow(num, 1);
                } else if (dartResult.charAt(i) == 'D') {
                    num = (int) Math.pow(num, 2);
                } else if (dartResult.charAt(i) == 'T') {
                    num = (int) Math.pow(num, 3);
                }
                i++;
                if (i < dartResult.length()) {
                    if (dartResult.charAt(i) == '*') {
                        num = num * 2;
                        if(j > 0) {
                           arr[j - 1] *= 2;
                        }
                        i++;
                    } else if (dartResult.charAt(i) == '#') {
                        num *= -1;
                        i++;
                    }
                }
                arr[j] = num;
                j++;
        }

        for (int k = 0; k < arr.length; k++) {
            sum += arr[k];
        }
        return sum;
    }
}