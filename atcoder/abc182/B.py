n = int(input())
lis = list(map(int,input().split()))
ans = 0
ansval = 0
for i in range(2,1001):
    tmp = 0
    for j in lis:
        if j%i==0:
            tmp+=1
    if tmp>ansval and i>=2:
        ans = i
    ansval = max(tmp,ansval)
print(ans)