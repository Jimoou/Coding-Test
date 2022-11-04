def solution(ingredient):
    ingredients = []
    count_Burger = 0
    for num in ingredient:
        ingredients.append(num)
        if ingredients[-4:] == [1, 2, 3, 1]:
            count_Burger += 1
            for num in range(4):
                ingredients.pop()
    return count_Burger