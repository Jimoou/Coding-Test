class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
            int currentHP = health;
    int lastAttackTime = attacks[attacks.length - 1][0];
    int count = 0;
    boolean attacked = false;

    for (int t = 1; t <= lastAttackTime; t++) {
      for (int i = 0; i < attacks.length; i++) {
        if (t == attacks[i][0]) {
          currentHP -= attacks[i][1];
          if (currentHP <= 0) {
            return -1;
          }
          attacked = true;
        }
      }
      if (attacked) {
        count = 0;
      } else {
        currentHP += bandage[1];
        count++;
        if (count == bandage[0]) {
          currentHP += bandage[2];
          count = 0;
        }
        if (currentHP > health) {
          currentHP = health;
        }
      }
      attacked = false;
    }
    return currentHP;
  }
}