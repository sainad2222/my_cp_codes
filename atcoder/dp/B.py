n, k = map(int, input().split())
lis = list(map(int,input().split()))
# dp = {}
def TD(i):
    if i in dp:
        return dp[i]
    if i == n-1:
        return 0
    mi = float('inf')
    for j in range(1, k + 1):
        if i + j < n:
            mi = min(mi, abs(lis[i + j] - lis[i]) + TD(i + j))
    dp[i] = mi
    return mi
# print(TD(0))

dp = [float('inf') for i in range(n)]
dp[0] = 0
for i in range(n):
    for j in range(1, k + 1):
        if i+j<n:
            dp[i+j] = min(dp[i+j], abs(lis[i] - lis[i +j]) + dp[i])
print(dp[n - 1])