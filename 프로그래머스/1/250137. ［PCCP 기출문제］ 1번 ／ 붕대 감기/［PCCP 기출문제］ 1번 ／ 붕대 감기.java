class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        
    int currentHP = health;
    int lastAttackTime = attacks[attacks.length - 1][0];
    int countinous = 0;
    boolean attacked = false;

    int t = 1;
    while (t <= lastAttackTime) {
      for (int[] attack : attacks) {
        if (t == attack[0]) {
          currentHP -= attack[1];
          if (currentHP <= 0) {
            return -1;
          }
          attacked = true;
        }
      }
      if (attacked) {
        countinous = 0;
      } else {
        currentHP += bandage[1];
        countinous++;
        if (countinous == bandage[0]) {
          currentHP += bandage[2];
          countinous = 0;
        }
        if (currentHP > health) {
          currentHP = health;
        }
      }
      attacked = false;
      t++;
    }
    return currentHP;
  }
}