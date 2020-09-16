for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    status = list(map(int,input().split()))
    res = [lis[i] for i in range(n) if status[i] == 0]
    res = sorted(res,reverse=True)
    k = 0
    for i in range(n):
        if status[i] == 0:
            lis[i] = res[k]
            k += 1
    print(*lis)