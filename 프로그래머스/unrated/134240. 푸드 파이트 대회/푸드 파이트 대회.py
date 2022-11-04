def solution(food):
    foodL = []
    foodR = []
    for i in range(1,len(food)):
        if food[i] > 1:
            foodL.append(str(i)*(food[i]//2))
            foodR.append(str(i)*(food[i]//2))
    foodL.append(0)
    result = foodL+sorted(foodR,reverse=True)
    return ''.join(map(str, result))