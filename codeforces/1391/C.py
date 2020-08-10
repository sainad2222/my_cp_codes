n = int(input())
mod = 10**9+7
fact = 1
for i in range(1, n + 1):
    fact = (fact * i) % mod
Ans = (fact-pow(2,n-1,mod))%mod
print(Ans)