def solution(price, money, count):
    result = sum([i for i in range(price, price*count+1, +price)]) - money
    if result < 0:
        return 0
    else:
        return result