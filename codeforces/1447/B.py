for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    cnt = 0
    mi = float('inf')
    ans = 0
    for i in range(n):
        tmp = list(map(int,input().split()))
        ans += (sum([abs(x) for x in tmp]))
        for j in tmp:
            if j < 0:
                cnt += 1
            mi = min(mi,abs(j))
    if cnt & 1:
        ans -= (2*mi)
    print(ans)