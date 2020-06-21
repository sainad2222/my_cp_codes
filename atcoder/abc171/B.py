n,k=map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
su = 0
for i in range(k):
    su += lis[i]
print(su)