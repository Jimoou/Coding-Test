class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int currentHP = health;
        int currentTime = 1;
        int attackIndex = 0;
        int continuous = 0;
        
        while (true) {
            boolean attacked = false;
            
            if (attackIndex < attacks.length && currentTime == attacks[attackIndex][0]) {
                currentHP -= attacks[attackIndex][1];
                if (currentHP <= 0) return -1;
                attackIndex++;
                attacked = true;
                continuous = 0;
            }
            if (!attacked) {
                if (continuous < bandage[0]) {
                    currentHP += bandage[1];
                    continuous++;
                }
                if (continuous == bandage[0]) {
                    currentHP += bandage[2];
                    continuous = 0;
                }
                if (currentHP > health) currentHP = health;
            }
            if (attackIndex >= attacks.length) {
                if (continuous == 0) break;
            } else {
                currentTime++;
            }
        }
        return currentHP;
    }
}