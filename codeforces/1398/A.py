for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    if lis[0] + lis[1] <= lis[-1]:
        print(1,2,n)
    else:
        print(-1)