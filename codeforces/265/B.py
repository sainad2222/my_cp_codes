n = int(input())
lis = []
for i in range(n):
    temp = int(input())
    lis.append(temp)
ans = len(lis)
ans+=lis[0]
for i in range(n-1):
    ans+=abs(lis[i]-lis[i+1])+1
print(ans)