def solution(common):
    gap = common[1] - common[0]
    return common[len(common) - 1] + gap if common[1] + gap == common[2] else common[len(common) - 1] * (common[1] // common[0])