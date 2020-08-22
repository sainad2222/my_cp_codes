n = int(input())
lis = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    if lis[i + 1] < lis[i]:
        ans+=(lis[i]-lis[i+1])
        lis[i + 1] += (lis[i] - lis[i+1])
print(ans)