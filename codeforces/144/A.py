n = int(input())
lis = list(map(int,input().split()))
res = []
ma,mi = max(lis),min(lis)
for i in range(n):
    if(lis[i]==ma):
        res.append(i)
        lis.remove(ma)
        lis.insert(0,ma)
        break
for i in range(n-1,-1,-1):
    if(lis[i]==mi):
        res.append(i)
        break
print(abs(res[0]-0)+abs(res[1]-(n-1)))