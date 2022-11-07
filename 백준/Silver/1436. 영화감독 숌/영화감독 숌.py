if __name__ == "__main__":
    N = int(input())
    answer = 665
    while N > 0:
        answer += 1
        if '666' in str(answer):
            N -= 1
    print(answer)