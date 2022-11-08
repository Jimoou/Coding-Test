if __name__ == '__main__':
    univ_W = []
    univ_K = []
    for _ in range(10): univ_W.append(int(input()))
    for _ in range(10): univ_K.append(int(input()))
    print(sum(sorted(univ_W,reverse=True)[:3]), sum(sorted(univ_K,reverse=True)[:3]))