def solve(lis,n):
    lis.sort()
    for i in range(1,n):
        if lis[i]-lis[i-1]>1:
            print("NO")
            return
    print("YES")
    return

for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    solve(lis,n)