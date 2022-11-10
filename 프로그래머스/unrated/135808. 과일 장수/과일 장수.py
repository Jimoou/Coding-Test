def solution(k, m, score):
    score.sort()

    sum = 0
    for packed in range(m,len(score)+1,m):
        box = list(score[-packed:len(score)-packed+m])
        sum += min(box)*m
    return sum