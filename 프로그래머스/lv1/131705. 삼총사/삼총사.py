def solution(number):
    from itertools import combinations as cb
    answer = 0
    for a in cb(number, 3):
        if sum(a) == 0:
            answer += 1
    return answer