import sys

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())

        scores = []
        for i in range(N):
            scores.append(list(map(int, sys.stdin.readline().split())))

        scores = sorted(scores)
        answer = 1
        index = scores[0][1]
        for i in range(1, N):
            if scores[i][1] < index:
                answer += 1
                index = scores[i][1]

        print(answer)
