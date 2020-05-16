n,m=map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
res=[]
for i in range(m-n+1):
    res.append(abs(lis[i]-lis[n-1+i]))
print(min(res))