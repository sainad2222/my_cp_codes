n, m = map(int, input().split())
res = []
su = 0
for i in range(n):
    a, b = map(int, input().split())
    res.append(b - a)
    su += a
res.sort()
i = 0
while su > m and i<len(res):
    su += res[i]
    i += 1
if i >= len(res) and su>m:
    print(-1)
else:
    print(i)