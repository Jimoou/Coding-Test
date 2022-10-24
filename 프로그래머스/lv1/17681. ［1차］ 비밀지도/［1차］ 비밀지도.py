def solution(n, arr1, arr2):
    s = [format(arr1[i]|arr2[i], 'b').rjust(n, "0") for i in range(n)]
    for i in range(len(s)):
        s[i] = s[i].replace(str(1), '#')
        s[i] = s[i].replace(str(0), ' ')
    return s