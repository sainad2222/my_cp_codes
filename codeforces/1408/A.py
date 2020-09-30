for _ in range(int(input())):
    n = int(input())
    res = []
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    res.append(a[0])
    first = a[0]
    prev = a[0]
    for i in range(1, n):
        if a[i] != prev and a[i]!=first:
            res.append(a[i])
            prev = a[i]
        elif b[i] != prev and b[i]!=first:
            res.append(b[i])
            prev = b[i]
        else:
            res.append(c[i])
            prev = c[i]
    print(*res)