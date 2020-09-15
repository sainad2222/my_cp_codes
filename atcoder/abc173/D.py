n = int(input())
lis = list(map(int,input().split()))
lis = sorted(lis, reverse=True)
ans = lis[0]
res = []
for i in range(1,n):
    res.append(lis[i])
    res.append(lis[i])
for i in range(n - 2):
    ans += res[i]
print(ans)