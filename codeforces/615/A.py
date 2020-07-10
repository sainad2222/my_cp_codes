n,m=map(int,input().split())
dic = [0]*m
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in range(1,len(tmp)):
        dic[tmp[i]-1]=1
if 0 in dic:
    print("NO")
else:
    print("YES")