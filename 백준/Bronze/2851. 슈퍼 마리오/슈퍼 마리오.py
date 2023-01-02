import sys

if __name__ == '__main__':
    score = []
    for _ in range(10):
        score.append(int(sys.stdin.readline()))

    pSum = [0 for i in range(len(score)+1)]
    max_gap = int(sys.maxsize)
    for i in range(1,len(pSum)):
        pSum[i] = pSum[i-1] + score[i-1]
        if abs(100-pSum[i]) <= max_gap:
            max_gap = abs(100-pSum[i])
            result = pSum[i]
    print(result)