def solution(strings, n):
    if len(strings) <= 1:
        return strings
    right = []
    left = []
    pivot = strings[0]
    for i in range (1, len(strings)):
        if strings[i][n] > pivot[n]:
            right.append(strings[i])
        elif strings[i][n] == pivot[n]:
            if strings[i] > pivot:
                right.append(strings[i])
            else:
                left.append(strings[i])
        else:
            left.append(strings[i])

    answer = []
    answer += solution(left, n)
    answer.append(pivot)
    answer += solution(right, n)
    return answer