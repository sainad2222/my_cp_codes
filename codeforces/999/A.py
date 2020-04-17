n,k = map(int,input().split())
lis = list(map(int,input().split()))
left,right = 0,0
for i in lis:
    if(i<=k):
        left+=1
    else:
        break
for i in range(len(lis)-1,0,-1):
    if(lis[i]<=k):
        right+=1
    else:
        break
print(min(n,left+right))
