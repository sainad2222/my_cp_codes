for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    for i in range(n):
        cur = lis[i]
        ans = 1
        while cur != i + 1:
            ans += 1
            cur = lis[cur - 1]
        print(ans, end=" ")
    print()