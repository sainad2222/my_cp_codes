n, w = map(int, input().split())
wt,val = [],[]
for i in range(n):
    x, y = map(int, input().split())
    wt.append(x)
    val.append(y)

dp = [[0 for i in range(w + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, w + 1):
        if wt[i-1]<=j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][w])