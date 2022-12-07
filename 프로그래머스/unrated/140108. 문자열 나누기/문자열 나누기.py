def solution(s):
    result = 0
    cnt1 = 0
    cnt2 = 0
    start = ""
    for i in range(len(s)):
        if start == "":
            start = s[i]

        if start == s[i]:
            cnt1 += 1
        else:
            cnt2 += 1

        if cnt1 == cnt2:
            result += 1
            cnt1 = 0
            cnt2 = 0
            start = ""
    if start:
        result += 1
    return result