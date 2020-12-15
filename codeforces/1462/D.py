def check(arr,n,ma):
    i = 0
    t = len(arr)
    cnt = 0
    cur = 0
    while i<t:
        cur += arr[i]
        if cur==ma:
            cnt += 1
            cur = 0
        elif cur>ma:
            return False
        i += 1
    if cur==ma:
        cnt += 1
    return cnt == n
for _ in range(int(input())):
    n = int(input())
    tmpn = n
    lis = list(map(int,input().split()))
    ma = max(lis)
    su = sum(lis)
    ans = 0
    while su%n != 0 or not check(lis,n,su//n):
        n -= 1
        if n==0:
            print("nope")
            break
    else:
        print(tmpn - n)
