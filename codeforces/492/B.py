n,l = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
prev = -1*lis[0]
ans = -1
for i in lis:
    ans = max(ans,(i-prev)/2)
    prev = i
ans=max(ans,l-lis[-1])
print('{0:.10f}'.format(ans))