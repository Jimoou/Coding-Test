def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left = i
            answer += "L"
        elif i == 3 or i == 6 or i == 9:
            right = i
            answer += "R"
        else:
            if i == 0:
                i = 11
            leftDistance = int(abs(i-left)/3 + abs(i-left)%3)
            rightDistance = int(abs(i-right)/3+abs(i-right)%3)
            if leftDistance > rightDistance:
                answer += "R"
                right = i
            elif leftDistance < rightDistance:
                answer += "L"
                left = i
            else:
                if hand == "left":
                    answer += "L"
                    left = i
                else:
                    answer += "R"
                    right = i

    return answer