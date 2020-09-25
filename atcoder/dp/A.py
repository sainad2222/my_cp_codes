n = int(input())
lis = list(map(int,input().split()))
# dp = {}
def TD(i):
    if i in dp:
        return dp[i]
    if i == n-1:
        return 0
    mi = float('inf')
    if (i < n - 1):
        mi = min(mi,abs(lis[i + 1] - lis[i]) + TD(i + 1))
    if i < n - 2:
        mi = min(mi,abs(lis[i + 2] - lis[i]) + TD(i + 2))
    dp[i] = mi
    return mi
# print(TD(0))

dp = [0 for i in range(n)]
dp[0] = 0
dp[1] = abs(lis[1] - lis[0])
for i in range(2, n):
    dp[i] = min(abs(lis[i] - lis[i - 1]) + dp[i - 1], abs(lis[i] - lis[i - 2]) + dp[i - 2])
print(dp[n-1])