n = int(input())
res = [0]
for i in range(n):
    l, r = map(int, input().split())
    res.append(l-r)
ma = max(res)
mi = min(res)
s = sum(res)
if ma+mi<s:
    print(res.index(mi))
else:
    print(res.index(ma))