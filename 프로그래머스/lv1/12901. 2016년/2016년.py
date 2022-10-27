def solution(a, b):
    day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return day[(sum(date[:a-1])+b+4)%7]