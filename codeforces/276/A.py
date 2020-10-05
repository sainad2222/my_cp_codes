n, k = map(int, input().split())
ma = -float('inf')
for i in range(n):
    f, t = map(int, input().split())
    if t > k:
        cur = f - (t - k)
    else:
        cur = f
    ma = max(ma, cur)
print(ma)