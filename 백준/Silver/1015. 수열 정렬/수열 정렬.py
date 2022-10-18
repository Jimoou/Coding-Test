input();
a = input().split();
b = sorted(a,key=int)
for i in a:
    p = b.index(i);
    print(p);
    b[p] = b