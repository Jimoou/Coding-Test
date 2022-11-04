def solution(food):
    left_Line = ''
    for i in range(1,len(food)):
        if food[i] > 1:
            left_Line += str(i)*(food[i]//2)
    right_Line = left_Line[::-1]
    left_Line += '0'
    return left_Line + right_Line