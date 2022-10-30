import math


def solution(nums):
    answer = 0
    num = []
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            for k in range (j+1,len(nums)):
                num.append(nums[i] + nums[j] + nums[k])
    for i in num:
        for k in range (2, int(math.sqrt(i)) + 1):
            if bool(i % k == 0):
                break
        else:
            answer += 1
    return answer