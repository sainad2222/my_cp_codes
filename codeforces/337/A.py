n,m=map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
msf=100000000
for i in range(m-n+1):
    res=abs(lis[i]-lis[n-1+i])
    msf = min(res,msf)
print(msf)