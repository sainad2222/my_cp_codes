n,m=map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
ans = 0
for i in range(m):
    if lis[i]<0:
        ans-=lis[i]
print(ans)