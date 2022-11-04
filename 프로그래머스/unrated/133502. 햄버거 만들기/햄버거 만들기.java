import java.util.Stack;
class Solution {
    public int solution(int[] ingredient) {
        Stack<Integer> ingredients = new Stack<>();
        int count_Burger = 0;
        for (int num = 0; num < ingredient.length; num++) {
            ingredients.push(ingredient[num]);
            int size = ingredients.size();
            if (size >3 && ingredients.peek() == 1
            && ingredients.get(size-2) == 3
            && ingredients.get(size-3) == 2
            && ingredients.get(size-4) == 1) {
                packaging_Burger(ingredients);
                count_Burger++;
            }
        }
        return count_Burger;
    }

    private static void packaging_Burger(Stack<Integer> ingredients) {
        ingredients.pop();
        ingredients.pop();
        ingredients.pop();
        ingredients.pop();
    }
}