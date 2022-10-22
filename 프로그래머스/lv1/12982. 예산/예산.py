def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in range(len(d)):
        budget -= d[i]
        if (budget < 0):
            break
        answer+=1
    return answer