def solution(s):
    english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    for x in english:
        s = s.replace(x, str(english.index(x)))

    return int(s)