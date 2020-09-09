for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    zcount = lis.count(0)
    ocount = n - zcount
    if zcount >= n // 2:
        print(zcount)
        print('0 ' * zcount)
    else:
        if ocount & 1:
            ocount -= 1
        print(ocount)
        print(ocount * '1 ')