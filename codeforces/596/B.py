# NTFS: Editorial 
n = int(input())
lis = list(map(int,input().split()))
lis = [0] + lis
ans = 0
for i in range(1,n+1):
    ans += abs(lis[i] - lis[i - 1])
print(ans)