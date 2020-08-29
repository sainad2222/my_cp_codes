n = int(input())
lis = list(map(int, input().split()))
mod = 1000000007
pre = [0] * n
su = 0
total = sum(lis)
for i in range(n):
    su += lis[i]
    pre[i] = su
suf = [0] * n
for i in range(n):
    suf[i] = total-pre[i]
ans = 0
for i in range(n):
    ans = (ans + (lis[i] * suf[i]) % mod) % mod
print(ans)