def solution(N, stages):
    di = {}
    temp = 0
    for i in range (1, N+1):
        if stages.count(i) != 0:
            di[i] = stages.count(i)/(len(stages)-temp)
        else:
            di[i] = 0
        temp += stages.count(i)
    return sorted(di, key=lambda x:di[x], reverse=True)