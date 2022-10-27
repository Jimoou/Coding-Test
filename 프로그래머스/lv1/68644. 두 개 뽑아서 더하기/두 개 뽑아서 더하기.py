def solution(numbers):
    answer = []
    for x in numbers:
        for j in range(numbers.index(x)+1, len(numbers)):
            answer.append(x + numbers[j])
    return sorted(list(set(answer)))