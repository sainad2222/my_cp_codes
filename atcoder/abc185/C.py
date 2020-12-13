def ncr(n, r):
    ans = 1
    for i in range(1, r+1):
        ans *= (n - r + i)
        ans //= i

    return ans
def NoOfDistributions(N, R):

    return ncr(N + R-1, R - 1)

n = int(input())
r = 12
print(NoOfDistributions(n-12,r))
