for _ in range(int(input())):
    n, k = map(int, input().split())
    lis = list(map(int,input().split()))
    lis.sort()
    ans = lis[-1]
    if n == 1:
        print(lis[0])
    i = n - 2
    while k > 0 and i >= 0:
        ans += lis[i]
        i -= 1
        k -= 1
    print(ans)