for _ in range(int(input())):
    n, k = map(int, input().split())
    lis = list(map(int, input().split()))
    d = max(lis)
    tmp1 = [d - x for x in lis]
    d = max(tmp1)
    tmp2 = [d-x for x in tmp1]
    if k & 1:
        print(*tmp1)
    else:
        print(*tmp2)