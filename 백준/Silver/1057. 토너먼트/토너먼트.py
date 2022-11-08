if __name__ == '__main__':
    N, jimin, hansoo = map(int, input().split())
    round = 1
    if jimin > hansoo:
        jimin, hansoo = hansoo, jimin

    while True:
        if jimin % 2 == 1 and hansoo - jimin == 1:
            break

        jimin = (jimin+1)//2
        hansoo = (hansoo+1)//2
        round += 1
    print(round)