def solution(arr):
    answer = []
    temp = -1
    for n in arr:
        if (temp != n):
            answer.append(n)
            temp = n
    return answer