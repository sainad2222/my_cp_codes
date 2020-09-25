for _ in range(int(input())):
    n, k = map(int, input().split())
    lis = list(map(int, input().split()))
    ans = 0
    lis = [0]+lis
    for i in range(n + 1):
        if lis[i] - lis[i - 1] > 0:
            ans+=(lis[i] - lis[i - 1])
    print(ans)