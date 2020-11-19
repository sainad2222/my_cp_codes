for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    ma = max(lis)
    su = sum(lis)
    ans = 0
    rem = (n-1) - su % (n - 1)
    x = ma * (n - 1) - su
    if su % (n - 1)==0:
        print(max(0, x))
        continue
    if x <= 0:
        print(rem)
        continue
    i = x
    while True:
        if (su + i) % (n - 1) == 0:
            print(i)
            break
        i+=1
