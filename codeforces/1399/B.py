def solve(a,b,n):
    ans = 0
    mina = min(a)
    minb = min(b)
    for i in range(n):
        ans += max(a[i]-mina,b[i]-minb)
    return ans

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(solve(a,b,n))