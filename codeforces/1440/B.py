def ceil(a, b):
    return (a + b - 1) // b
for _ in range(int(input())):
    n, k = map(int, input().split())
    lis = list(map(int, input().split()))
    lis = lis[::-1]
    mid = n//2
    ans = 0
    cnt = 0
    for i in range(mid, n * k, mid + 1):
        if cnt<k:
            ans += lis[i]
            # print(lis[i])
            cnt+=1
    print(ans)