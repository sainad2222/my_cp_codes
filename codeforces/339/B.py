n,m=map(int,input().split())
lis = list(map(int,input().split()))
time=0
for i in range(m-1):
    if(lis[i]<=lis[i+1]):
        time+=lis[i+1]-lis[i]
    else:
        time+=n-lis[i]+lis[i+1]
time+=lis[0]-1
print(time)