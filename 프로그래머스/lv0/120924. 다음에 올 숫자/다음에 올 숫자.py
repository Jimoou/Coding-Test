def solution(common):
    gap = common[1] - common[0]
    if common[1] + gap == common[2]:
        answer = common[len(common) - 1] + gap
    else:
        gap = common[1] // common[0]
        answer = common[len(common) - 1] * gap
    return answer